from django.core.management.base import BaseCommand

from feh.crawler import crawl_heroes


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__('test_crawler')

    def handle(self, *args, **options):
        crawl_heroes()
