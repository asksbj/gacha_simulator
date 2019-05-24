from commons.gacha import gacha_rarity

from .models import Heroes


def feh_gacha(num=5, gacha_pool='common'):
    rarity_heroes = dict()
    rarity_map = dict()

    if gacha_pool == 'common':
        rarity_heroes['3'] = list(Heroes.objects.filter(rarity_low__lte=3, rarity_high__gte=3).values_list('name', flat=True))
        rarity_heroes['4'] = list(Heroes.objects.filter(rarity_low__lte=4, rarity_high__gte=4).values_list('name', flat=True))
        rarity_heroes['5'] = list(Heroes.objects.filter(rarity_low__lte=5, rarity_high__gte=5).values_list('name', flat=True))

        rarity_map['3'] = 0.36
        rarity_map['4'] = 0.58
        rarity_map['5'] = 0.06

        return gacha_rarity(rarity_heroes, rarity_map, num)



