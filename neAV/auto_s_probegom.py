import json
import requests
from bs4 import BeautifulSoup
import sqlite3

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

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

def get_auto(mark):

    urls = f'https://cars.av.by/{mark}'

    r = requests.get(urls, headers=headers)
    auto = BeautifulSoup(r.content, "html.parser")

    data = auto.find_all("div", class_="listing__items")

    for el in data:
        elem = el.find_all("div", class_="listing-item__wrap")
        for dat in elem:
            cart_url = 'https://cars.av.by' + dat.find("a").get("href")
            yield cart_url

for mark in list_1:
    try:
        for cart_url in get_auto(mark):

            FOREIGN_KEY = 1

            conn = sqlite3.connect('db.sqlite3')

            r = requests.get(cart_url, headers=headers)
            auto2 = BeautifulSoup(r.content, "html.parser")

            data2 = auto2.find('div', class_='card')

            name = data2.find('h1', class_="card__title").text.replace('Продажа ', '')
            number_post = data2.find('ul', class_='card__stat').text.split('№')[-1].replace(' ', '')

            r2 = requests.get('https://api.av.by/offers/' + number_post, headers=headers)
            formatos = r2.json()['photos']
            photo = formatos[0]['big']['url']

            price_for_bel_rub = data2.find('div', class_='card__price-primary').text.split('р.')[0]
            price_for_usd = data2.find('div', class_='card__price-secondary').text.split('$')[0]
            params = data2.find('div', class_='card__params').text.split(',')
            year = params[0]
            kpp = params[1]
            volume = params[2]
            type_engine = params[3]
            probeg = params[4]
            description = data2.find('div', class_='card__description').text.split(',')
            kyzov = description[0]
            privod = description[1]
            color1 = description[2]
            modification = data2.find('div', class_='card__modification')
            power = str(modification.find('span').text.split('.,'))
            comment = data2.find('div', class_='card__comment-text').text
           # print(name, price_for_bel_rub, price_for_usd, photo, year, kpp, volume, type_engine, probeg, kyzov, privod, color1, power, comment, FOREIGN_KEY)
            cursor = conn.cursor()
            insert_query = """INSERT INTO "Used_auto" (
                                                        name, 
                                                        price_for_bel_rub,
                                                        price_for_usd,
                                                        photo,
                                                        year,
                                                        kpp,
                                                        volume,
                                                        type_engine,
                                                        probeg,
                                                        kyzov,
                                                        privod,
                                                        color,
                                                        power,
                                                        comment,
                                                        addcat_id
                                                        )
                                                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(insert_query, (name, price_for_bel_rub, price_for_usd, photo, year, kpp, volume, type_engine, probeg, kyzov, privod, color1, power, comment, FOREIGN_KEY))
            conn.commit()
    except Exception as e:
        print(e)
        continue


# import re, time, urllib2

# url = "http://lenta.ru/"
# content = urllib2.urlopen(url).read()
# imgUrls = re.findall('img .*?src="(.*?)"', сontent)

# start = time.time()
# for img in imgUrls:
#     if img.endswith(".jpg"):
#         """реализация метода по загрузке изображения из url"""

# print time.time()-start