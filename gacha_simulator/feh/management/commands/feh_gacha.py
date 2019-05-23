from django.core.management.base import BaseCommand

from feh.gacha import feh_gacha


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__('test_crawler')

    def handle(self, *args, **options):
        stars, heroes = feh_gacha()
        for i in range(0, len(heroes)):
            print('Hero - {}, Star - {}'.format(heroes[i], stars[i]))
