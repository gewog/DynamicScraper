import json
import time

import lxml
import undetected_chromedriver

from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

url = "https://www.ozon.ru/product/shtora-dlya-kuhni-45h137-sm-krasnyy-belyy-2873484548/?at=J8tgZQqj3sYGWppoCgpALvwCM6w3LpTXlv94xHjA53yN&tab=reviews"
url2 = "https://www.ozon.ru/product/shtora-32h300-sm-belyy-2870181183/?at=lRt6xz1GyuLoRr1JcKwY6NJTkEDo8MhnNAVVmfz3m9AW"




# def get_info_about_orig(url):
#     with undetected_chromedriver.Chrome() as cr:
#         cr.get(url)
#         time.sleep(1)
#         # Блок кода по получению данных
#         artik = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[2]/div/div/div/div[2]/button[1]/div").text.split(" ")[1]
#         name = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/h1").text
#         # Получаю рейтинг
#         try:
#             rating = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/button/div").text
#             if rating == "Нет отзывов":
#                 rating = 0
#         except:
#             rating = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/a/div").text.split(" ")[0]
#         print(3)
#
#         # Получаю кол-во отзывов
#         try:
#             reviews_num = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/button/div").text.lower()
#         except:
#             reviews_num = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/a/div").text.split("•")[1].strip()
#         try:
#             price = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/span").text.split(" ")[0]
#         except:
#             try:
#                 price = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div/div[1]/span[1]").text
#             except:
#                 price = 0
#
#         full_info = {"id": artik,
#                      "name": name,
#                      "rating": rating,
#                      "reviews_num": reviews_num,
#                      "price": "".join(list(filter(str.isdigit, price)))
#                      }
#         return full_info
md = {'https://www.ozon.ru/product/shtora-150h260-sm-belyy-2869617131/?at=XQtk2MDEBFGlxgKNFP1JPyksWOpWAVu54x23oCqB8vD9',
      'https://www.ozon.ru/product/shtora-89h213-sm-rozovyy-2873340485/?at=J8tgZQA9phyVQv0DI0ZP2qNUgVvnyYcqAJLrWty2LkEV',
      'https://www.ozon.ru/product/komplekt-shtor-shtory-blekaut-600h200-sm-bezhevyy-2869400772/?at=NOtw7MPkVcvJ22G6t219MGquqYqwlLTGVAVy0tJVkXEy',
      'https://www.ozon.ru/product/shtora-160h210-sm-belyy-2863475530/?at=Z8tXlo8KPhyZRx35U7YAwoAuVMRAJcMG2z6RhVEkpNL',
      'https://www.ozon.ru/product/shtora-h210-sm-rozovyy-2865982536/?at=Vvtz3Pkq0Tr6OYQmFq4LG4KsMZEqvZHP8Ezo8fY3GzqX'}

def get_info_about(md):
    emt_l = []
    chrome_options = undetected_chromedriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")  # Раскомментируй для фонового режима
    with undetected_chromedriver.Chrome(options=chrome_options) as cr:
        for el in md:
            cr.get(el)
            time.sleep(1)
            # Блок кода по получению данных
            artik = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[2]/div/div/div/div[2]/button[1]/div").text.split(" ")[1]
            time.sleep(1)
            name = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/h1").text
            time.sleep(1)
            # Получаю рейтинг
            try:
                rating = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/button/div").text
                if rating == "Нет отзывов":
                    rating = 0
            except:
                rating = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/a/div").text.split(" ")[0]
            time.sleep(1)

            # Получаю кол-во отзывов
            try:
                reviews_num = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/button/div").text.lower()
            except:
                reviews_num = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[1]/a/div").text.split("•")[1].strip()
            time.sleep(1)
            try:
                price = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/span").text.split(" ")[0]
            except:
                try:
                    price = cr.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div/div[1]/span[1]").text
                except:
                    price = 0

            full_info = {"id": artik,
                         "name": name,
                         "rating": rating,
                         "reviews_num": reviews_num,
                         "price": "".join(list(filter(str.isdigit, price)))
                         }
            emt_l.append(full_info)
        return emt_l


if __name__ == "__main__":
    try:
        print(get_info_about(md))
    except Exception as e:
        print(e)








