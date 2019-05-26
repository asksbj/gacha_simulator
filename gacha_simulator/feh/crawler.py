import re
import html

from django.db import transaction

from commons.crawler import open_url, save_images
from .models import Heroes, Pools

BASE_URL = 'https://feheroes.gamepedia.com/'


def crawl_heroes():
    hero_list_url = BASE_URL + 'List_of_Heroes'
    hero_list_result = open_url(hero_list_url).decode('utf-8')

    hero_list_patten = re.compile(r'<td><a href="/([^"]+)" title="([^"]+)"><img alt="([^"]+)" src="([^"]+)" ')

    items = hero_list_patten.findall(hero_list_result)

    for item in items:
        columns = {}

        hero_url, hero_name, image_name, image_address = item

        columns['image'] = html.unescape(image_name)

        hero_url = BASE_URL + hero_url

        hero_result = open_url(hero_url).decode('utf-8')

        columns['rarity_low'] = int(re.search(r'vertical-align:bottom">\d<img alt=', hero_result).group(0)[23:24])
        columns['rarity_high'] = 4 if columns['rarity_low'] <= 3 else 5

        _, columns['art_by'] = re.findall(r'[ |;]<a href="([^"]+)" title="([^"]+)">', hero_result)[0]

        type_properties = re.findall(r'>&#160;<a href="([^"]+)" title="([^"]+)">', hero_result)[:2]
        _, weapon_type = type_properties[0]
        columns['weapon_type'] = weapon_type
        _, move_type = type_properties[1]
        columns['move_type'] = move_type

        other_properties = re.findall(r'vertical-align:bottom"> <a href="([^"]+)" title="([^"]+)">', hero_result)[:3]
        _, columns['appears_in'] = other_properties[0]
        if len(other_properties) >= 3:
            _, columns['voice_actor'] = other_properties[2]

        for key, value in Heroes.COLOR_WEAPON_MAPPING.items():
            if columns['weapon_type'] in value:
                columns['hero_type'] = key
                break

        columns['release_date'] = re.search(r'<time datetime="([^"]+)"', hero_result).group(0)[16:26]
        columns['description'] = re.search(r'vertical-align:bottom"> ([^<]+)</div', hero_result).group(0)[24:-5]

        hero_name = html.unescape(hero_name)
        print('Processing hero {}'.format(hero_name))
        with transaction.atomic():
            Heroes.objects.update_or_create(name=hero_name, defaults=columns)

            save_images('feh', image_name, image_address)


def crawl_pools():
    pool_list_url = BASE_URL + 'Summoning_Focus_archive'
    pool_list_result = open_url(pool_list_url).decode('utf-8')

    pool_list_patten = re.compile(
        r'style="text-align:center;width:33%"><a href="/([^"]+)" title="([^"]+)"><img alt="([^"]+)" src="([^"]+)" ')

    items = pool_list_patten.findall(pool_list_result)
    for item in items:
        columns = {}

        pool_url, pool_name, pool_image_name, pool_image_address = item
        pool_name = html.unescape(pool_name)

        columns['url_name'] = html.unescape(pool_url)
        columns['image'] = html.unescape(pool_image_name)

        pool_url = BASE_URL + pool_url

        pool_result = open_url(pool_url).decode('utf-8')

        # print(pool_result)

        rarity_parttern = re.compile(
            r'<td>5★ Focus</td><td>([^%"]+)%</td></tr><tr><td>5★</td><td>([^%"]+)%</td></tr><tr><td>4★</td><td>([^%"]+)'
            r'%</td></tr><tr><td>3★</td><td>([^%"]+)%</td></tr></tbody>')
        rarity_items = rarity_parttern.findall(pool_result)
        if not rarity_items:
            continue
        rarity_item = rarity_items[-1]

        start5_focus, start5, start4, start3 = rarity_item

        columns['start5_focus'] = float(re.sub('[^0-9.]', '0', start5_focus))/100
        columns['start5'] = float(re.sub('[^0-9.]', '0', start5)) / 100
        columns['start4'] = float(re.sub('[^0-9.]', '0', start4)) / 100
        columns['start3'] = float(re.sub('[^0-9.]', '0', start3)) / 100

        pool_hero_patten = re.compile(r'</span><a href="/([^"]+)" title="([^"]+)"><img alt="" src="([^"]+)" ')

        hero_items = pool_hero_patten.findall(pool_result)

        hero_set = set()
        for hero_item in hero_items:
            hero_url, hero_name, image_address = hero_item

            hero_set.add(html.unescape(hero_name))

        print('Processing pool {}'.format(pool_name))
        with transaction.atomic():
            pool, created = Pools.objects.update_or_create(name=pool_name, defaults=columns)

            if created:
                for hero_name in hero_set:
                    hero = Heroes.objects.get(name=hero_name)
                    pool.heroes.add(hero)

            save_images('feh', pool_image_name, pool_image_address)







