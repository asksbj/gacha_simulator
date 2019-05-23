import urllib.request
import random


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
    html = response.read().decode('utf-8')
    return html


def set_proxy_support(proxy_ip):
    proxy_support = urllib.request.ProxyHandler({'http': proxy_ip})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
