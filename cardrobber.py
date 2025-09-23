"""
Модуль для сбора информации о товарах с сайта Ozon.

Этот модуль предоставляет функцию для получения информации о товаре по его URL,
включая артикул, название, рейтинг, количество отзывов и цену.
Используются библиотеки: `selenium`, `undetected_chromedriver`, `BeautifulSoup`.
"""

import json
import time

import lxml
import undetected_chromedriver

from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


def get_info_about(md: set[str]) -> list[dict[str, str | int]]:
    """
    Собирает информацию о товарах по их URL.

    Аргументы:
        md (set[str]): Множество URL-адресов товаров, информацию о которых нужно собрать.

    Возвращает:
        list[dict[str, str | int]]: Список словарей, где каждый словарь содержит информацию о товаре:
            - id (str): Артикул товара.
            - name (str): Название товара.
            - rating (str | int): Рейтинг товара. Если отзывов нет, значение равно 0.
            - reviews_num (str): Количество отзывов.
            - price (str): Цена товара (только цифры).

    Описание:
        1. Открывает браузер Chrome с использованием `undetected_chromedriver`.
        2. Для каждого URL из множества `md` переходит на страницу товара.
        3. Собирает информацию об артикуле, названии, рейтинге, количестве отзывов и цене.
        4. Возвращает список словарей с собранной информацией.
    """
    emt_l: list[dict[str, str | int]] = []
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









