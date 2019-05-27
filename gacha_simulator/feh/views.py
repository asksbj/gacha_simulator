from django.shortcuts import render

from .models import Heroes, Pools
from .gacha import feh_gacha


def index(request):
    pools = Pools.objects.all()
    return render(request, 'feh/index.html', {'pools': pools})


def gacha(request, pool_name=None):
    pool = Pools.objects.get(url_name=pool_name)
    return render(request, 'feh/gacha.html', {'pool': pool})


def gacha_result(request, pool_name=None):
    result = {}
    pool_name = pool_name
    num = request.POST.get('number')

    rarities, heroes = feh_gacha(num=int(num), gacha_pool=pool_name)
    result['rarities'] = rarities
    result['heroes'] = heroes

    images = []
    for hero in heroes:
        hero = Heroes.objects.get(name=hero)
        images.append(hero.image)

    result['images'] = images

    result['pool'] = pool_name
    result['number'] = num

    return render(request, 'feh/gacha_result.html', result)
