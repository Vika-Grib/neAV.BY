import requests
from bs4 import BeautifulSoup as bs
import json
import sqlite3

list_1 = ['apollo', 'Fuego', 'KTM', 'Racer', 'Yamaha', 'Aprilia', 'gas-gas',
          'KXD', 'Regulmoto', 'YCF', 'Beta',  'Husaberg', 'Motax', 'SSSR', 'voshod', 'BMW']

# url_audi = 'https://api.av.by/offer-types/cars/landings/audi'
# url_1 = 'https://pzz.by/api/v1/snacks?load=modifications&filter=meal_only:0,parent_id:is:null&order=position:asc'

# парсим с сайта av.by / ntework / fetch (headers, response)
def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    print(url)
    current_page_auto = resp.json()['seo']['links']
    print(current_page_auto)
    # input()
    auto_data = ''
    for auto in current_page_auto:
        print(auto)
        auto_url = auto['url']
        label = auto['label']
        count = auto['count']
        popular = auto['popular']
        auto_data += str(auto_url) + ' ' + str(label) + ' ' + str(count) + ' ' + str(popular) + '\n'

    # for label in auto_data:
    #     print(label)
    return auto_data

for mark in list_1:
    file = open(f'./neAV/moto/{mark}.txt', 'w', encoding='utf-8')
    auto_info_list = get_content(f'https://api.av.by/offer-types/moto/landings/bike/{mark}')
    file.write(auto_info_list)
    file.close()









