from django.db.models import Q

from commons.gacha import gacha_rarity

from .models import Heroes, Pools


def feh_gacha(num=5, gacha_pool='common'):
    rarity_heroes = dict()
    rarity_map = dict()

    if gacha_pool == 'common':
        rarity_heroes['3'] = list(
            Heroes.objects.filter(rarity_low__lte=3, rarity_high__gte=3).values_list('name', flat=True))
        rarity_heroes['4'] = list(
            Heroes.objects.filter(rarity_low__lte=4, rarity_high__gte=4).values_list('name', flat=True))
        rarity_heroes['5'] = list(
            Heroes.objects.filter(rarity_low__lte=5, rarity_high__gte=5).values_list('name', flat=True))

        rarity_map['3'] = 0.36
        rarity_map['4'] = 0.58
        rarity_map['5'] = 0.06

    else:
        pool = Pools.objects.get(Q(url_name=gacha_pool) | Q(name=gacha_pool))
        focus_heroes = list(pool.heroes.all().values_list('name', flat=True))
        rarity_heroes['3'] = list(
            Heroes.objects.filter(rarity_low__lte=3, rarity_high__gte=3).values_list('name', flat=True))
        rarity_heroes['4'] = list(
            Heroes.objects.filter(rarity_low__lte=4, rarity_high__gte=4).values_list('name', flat=True))
        rarity_heroes['5'] = list(
            Heroes.objects.filter(rarity_low__lte=5, rarity_high__gte=5).exclude(name__in=focus_heroes).values_list('name', flat=True))
        rarity_heroes['5_focus'] = focus_heroes

        rarity_map['3'] = pool.start3
        rarity_map['4'] = pool.start4
        rarity_map['5'] = pool.start5
        rarity_map['5_focus'] = pool.start5_focus

    rarities, heroes = gacha_rarity(rarity_heroes, rarity_map, num)
    rarities = [rarity if rarity != '5_focus' else '5' for rarity in rarities]

    return rarities, heroes



