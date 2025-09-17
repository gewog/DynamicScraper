import time
import json
import lxml
import undetected_chromedriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from fake_useragent import UserAgent

agent = UserAgent.random

task_url = "https://www.ozon.ru/"
item = "шторы"


def scroll_func(uc) -> None:
    """
      Прокручивает страницу вниз для загрузки дополнительного контента.

      Аргументы:
          uc (selenium.webdriver.Chrome): Экземпляр веб-драйвера Chrome.

      Возвращает:
          None
      """
    time.sleep(2)
    uc.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(2)


def get_products_links(url, item) -> list:
    """
    Собирает ссылки на товары с сайта Ozon по заданному поисковому запросу.

    Аргументы:
        url (str): Базовый URL сайта Ozon.
        item (str): Поисковый запрос для поиска товаров.

    Возвращает:
        list: Список ссылок на товары.

    Описание:
        1. Открывает браузер Chrome с использованием undetected_chromedriver.
        2. Переходит на сайт Ozon.
        3. Вводит поисковый запрос и нажимает кнопку поиска.
        4. Фильтрует результаты по категории "Новинки".
        5. Прокручивает страницу для загрузки дополнительных товаров.
        6. Собирает ссылки на товары и возвращает их в виде списка.
    """
    emt_l = []  # Список для хранения ссылок на товары
    with undetected_chromedriver.Chrome() as uc:
        uc.implicitly_wait(10)  # Устанавливаем неявное ожидание для поиска элементов
        uc.get(url)  # Переход на сайт Ozon
        time.sleep(4)

        # Поиск поля ввода и кнопки поиска
        # input_field = uc.find_element(By.CSS_SELECTOR, ".t8n_30.tsBody500Medium")
        input_field = uc.find_element(By.CSS_SELECTOR, 'input[placeholder="Искать на Ozon"]')
        print(1)
        input_button = uc.find_element(By.CSS_SELECTOR, 'button[aria-label="Поиск"]')
        print(2)
        input_field.clear()  # Очистка поля ввода
        input_field.send_keys(item)  # Ввод данных
        time.sleep(2)
        input_button.click()  # Нажатие кнопки поиска
        time.sleep(2)

        # Выбор категории "Новинки"
        dropdown_list = uc.find_element(By.XPATH, "//input[@value='Популярные']")
        dropdown_list.click()
        time.sleep(2)
        res = uc.find_element(By.XPATH, "//span[text()='Новинки']")
        res.click()
        time.sleep(2)

        for el in range(2):
            scroll_func(uc)
            links = uc.find_elements(By.CSS_SELECTOR, 'a[href*="/product/"]')
            for el in links:
                emt_l.append(el.get_attribute("href"))

        print("Ссылки на товары собраны")
        print(emt_l)

        uc.quit()  # Завершаем работу

    return emt_l


# def main():
#     get_products_links()

if __name__ == "__main__":
    try:
        # scroll_func(task_url)
        get_products_links(task_url, item)
    except Exception as e:
        print(e)
