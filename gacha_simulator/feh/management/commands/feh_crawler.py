from django.core.management.base import BaseCommand

from feh.crawler import crawl_heroes, crawl_pools


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__('test_crawler')

    def add_arguments(self, parser):
        parser.add_argument('--target', type=str, dest='target', default='hero', help='Crawler Target')

    def handle(self, *args, **options):
        if options['target'] == 'hero':
            crawl_heroes()
        elif options['target'] == 'pool':
            crawl_pools()
