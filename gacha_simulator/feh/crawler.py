import re

from commons.crawler import open_url
from .models import Heroes


def crawl_heroes():
    base_url = 'https://feheroes.gamepedia.com/'

    hero_list_url = base_url + 'List_of_Heroes'
    hero_list_result = open_url(hero_list_url)

    hero_list_patten = re.compile(r'<td><a href="/([^"]+)" title="([^"]+)"><')

    items = hero_list_patten.findall(hero_list_result)

    for item in items:
        columns = {}

        hero_url, hero_name = item

        hero_url = base_url + hero_url

        hero_result = open_url(hero_url)

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

        print('Processing hero {}'.format(hero_name))
        Heroes.objects.update_or_create(name=hero_name, defaults=columns)


