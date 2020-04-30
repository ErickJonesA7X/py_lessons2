import json
import requests
from mtgsdk import Card

# partial name match
# cards = Card.where(name='avacyn').all()

# exact name match

cache = dict()


def get_card_image_url_by_name(name):
    if name in cache:
        return cache[name].image_url
    cards = Card.where(name=f'"{name}"').all()
    for c in cards:
        if c.image_url:
            cache[name] = c
            return c.image_url


def get_card_oracle_text_by_name(name):
    if name in cache:
        return cache[name].text
    cards = Card.where(name=f'"{name}"').all()
    c = cards[0]
    cache[name] = c
    return c.text



# api_url = 'https://api.magicthegathering.io/v1/cards'
# response = requests.get(api_url)
#
# if response.status_code == 200:
#     json_response = json.loads(response.content.decode('utf-8'))
#     print(json_response)
# else:
#     print('erro')

if __name__ == '__main__':
    print(get_card_image_url_by_name('Sol Ring'))
    print(get_card_oracle_text_by_name('Sol Ring'))
