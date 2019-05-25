import urllib.request
import os
import random

from django.conf import settings


def open_url(url, data=None):

    header = dict()
    header['user-agent'] = \
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    proxies = ['157.230.149.189:80', '35.247.204.72:80', '157.230.226.113:8080', '67.205.151.211:3128']
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url, data, header)
    response = urllib.request.urlopen(req)
    html_centent = response.read()
    return html_centent


def set_proxy_support(proxy_ip):
    proxy_support = urllib.request.ProxyHandler({'http': proxy_ip})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


def save_images(app_path, image_name, image_address):
    filename = 'static/' + app_path + '/img/' + image_name
    filename = os.path.join(settings.BASE_DIR, filename)
    with open(filename, 'wb') as file:
        img = open_url(image_address)
        file.write(img)
