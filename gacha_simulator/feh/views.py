from django.shortcuts import render

from .models import Heroes
from .gacha import feh_gacha


def index(request):
    return render(request, 'feh/index.html')


def gacha_result(request):
    result = {}
    print(request.POST)
    num = request.POST.get('number')
    rarities, heroes = feh_gacha(num=int(num))
    result['rarities'] = rarities
    result['heroes'] = heroes

    images = []
    for hero in heroes:
        hero = Heroes.objects.get(name=hero)
        images.append(hero.image)

    result['images'] = images

    return render(request, 'feh/gacha_result.html', result)
