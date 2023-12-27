import requests
from bs4 import BeautifulSoup as bs
import json
import sqlite3

list_1 = ['abarth', 'denza', 'iran-khodro', 'mitsubishi', 'suzuki', 'acura', 'derways',
          'isuzu', 'nio', 'tata', 'aeolus', 'dodge', 'jac', 'nissan', 'tesla', 'aito', 'dong-feng',
          'jaguar', 'oldsmobile', 'toyota', 'alfa-romeo', 'dongfeng-honda', 'jeep', 'omoda',
          'trabant', 'asia', 'exeed', 'jetour', 'opel', 'vgv', 'aston-martin', 'faw', 'jetta', 'peugeot',
          'volkswagen', 'audi', 'ferrari', 'jiangling', 'plymouth', 'volvo', 'avart', 'fiat', 'joylong',
          'polestar', 'vortex', 'baic', 'ford', 'kaiyi', 'pontiac', 'voyah', 'baojun', 'fso', 'kia', 'porsche',
          'wartburg', 'bentley', 'gac', 'lada-vaz', 'proton', 'weltmeister', 'bmw', 'geely', 'lamborghini',
          'ram', 'xpeng', 'brilliance', 'genesis', 'lancia', 'ravon', 'zeekr', 'buick', 'gmc', 'land-rover',
          'renault', 'zotye', 'byd', 'great-wall', 'leapmotor', 'renault-samsung', 'cadillac', 'hafei',
          'lexus', 'roewe', 'changan', 'haima', 'lifan', 'rover', 'zaz', 'chery', 'haval', 'lincoln', 'saab',
          'chevrolet', 'hiphi', 'lixiang', 'saturn', 'chrysler', 'honda', 'lotus', 'scion', 'citroen',
          'hongqi', 'maserati', 'seat', 'cupra', 'hozon', 'mazda', 'skoda', 'dacia', 'hummer', 'mercedes-benz',
          'skywell', 'eksklyuziv', 'daewoo', 'hycan', 'mercury', 'smart', 'daihatsu', 'hyundai', 'mg', 'ssangyong',
          'datsun', 'infiniti', 'mini', 'subaru']

# url_audi = 'https://api.av.by/offer-types/cars/landings/audi'
# url_1 = 'https://pzz.by/api/v1/snacks?load=modifications&filter=meal_only:0,parent_id:is:null&order=position:asc'

# парсим с сайта av.by / ntework / fetch (headers, response)
def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
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
file = open('auto.txt', 'w', encoding='utf-8')
for mark in list_1:
    auto_info_list = get_content(f'https://api.av.by/offer-types/cars/landings/{mark}')
    file.write(auto_info_list)
file.close()









