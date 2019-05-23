import random


def gacha_comman(rate_map, num=1):
    result_list = []

    key_list = list(rate_map.keys())

    for i in range(num):
        rand = random.random()

        rate_total = 0
        for key in key_list:
            rate_total += rate_map[key]
            if rand < rate_total:
                result_list.append(key)
                break
    return result_list


def gacha_rarity(rarity_items, rarity_map, num):
    gacha_list = gacha_comman(rarity_map, num)

    result_list = []
    for rarity in gacha_list:
        item_list = rarity_items.get(rarity)

        rand = random.randint(0, len(item_list)-1)
        result_list.append(item_list[rand])

    return gacha_list, result_list

