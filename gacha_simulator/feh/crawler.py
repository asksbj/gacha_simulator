from crawler.crawler import open_url


def main():
    header = {}
    header['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    result = open_url('https://fireemblem.gamepress.gg/hero', header=header)
    print(result)


if __name__ == 'main':
    main()
