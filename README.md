<div align="center">
  <h1>DynamicScraper</h1>
  <p>
    <strong>Динамический парсер товаров с Ozon</strong>
  </p>
  <p>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
    </a>
    <a href="https://python.org">
      <img src="https://img.shields.io/badge/python-3.13+-blue.svg" alt="Python Version">
    </a>
  </p>
</div>

---

## 🎯 Цель проекта
**DynamicScraper** — это инструмент для автоматического сбора данных о товарах с платформы [Ozon](https://www.ozon.ru/). Проект позволяет:
- **Собирать ссылки** на товары по поисковому запросу.
- **Парсить информацию** о товаре: название, артикул, рейтинг, количество отзывов и цену.
- **Сохранять данные** в удобном формате `JSON` для дальнейшего анализа.

Идеально подходит для маркетологов, аналитиков и разработчиков, которым необходим быстрый сбор актуальных данных о товарах.

---

## 🛠 Стек технологий
| Категория          | Технологии                                                                 |
|--------------------|----------------------------------------------------------------------------|
| **Язык**          | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) 3.13+ |
| **Парсинг**       | Selenium, Undetected Chromedriver, BeautifulSoup, lxml                     |
| **Управление зависимостями** | ![Poetry](https://img.shields.io/badge/-Poetry-60A5FA?logo=poetry&logoColor=white) |
| **Форматирование** | Slugify, JSON                                                             |
| **Контейнеризация** | ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white) |

---

## ⚙ Установка и запуск

### 📥 Предварительные требования
1. Установите [Python 3.13+](https://www.python.org/downloads/).
2. Установите [Poetry](https://python-poetry.org/docs/#installation) для управления зависимостями.
3. (Опционально) Установите [Docker](https://www.docker.com/get-started), если планируете запускать проект в контейнере.

---

### 🚀 Локальная установка
1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/gewoggewog/DynamicScraper.git
   cd DynamicScraper
   ```
2. **Установите зависимости:**
   ```bash
    poetry install
   ```
3. **Запустите скрипт:**
   ```bash
   poetry run python main.py
   ```

### 🐳 Запуск через Docker
1. **Соберите образ:**
   ```bash
   docker build -t dynamicscraper .
   ```
2. **Запустите контейнер:**
   ```bash
    docker run --rm dynamicscraper
   ```
   
### 📂 Структура проекта
```
DynamicScraper/
├── cardrobber.py          # Модуль для сбора информации о товарах
├── main.py                # Основной скрипт для парсинга ссылок и данных
├── pyproject.toml         # Конфигурация Poetry
├── poetry.lock            # Зафиксированные зависимости
├── README.md              # Документация проекта
├── requirements.txt       # Зависимости для pip
├── about_products_*.json  # Результаты парсинга информации о товарах
└── products_*.json        # Результаты сбора ссылок на товары
   ```


### 🎬 Пример работы
1. **Сбор ссылок на товары:**
   Скрипт `main.py` собирает ссылки на товары по запросу (например, "barbie") и сохраняет их в файл `products_barbie_url.json`:
   ```json
   {
     "0": "https://www.ozon.ru/product/barbie-1-123456789/",
     "1": "https://www.ozon.ru/product/barbie-2-987654321/"
   }
   ```

2. **Парсинг информации о товарах:**


   Модуль cardrobber.py собирает детальную информацию о каждом товаре и сохраняет её в about_products_barbie.json:
   ```bash
    [
    {
    "id": "123456789",
    "name": "Кукла Барби Classic",
    "rating": "4.8",
    "reviews_num": "125 отзывов",
    "price": "1999"
     }
     ]
   ```

## 📎 Ссылки для скачивания
- **[ChromeDriver](https://chromedriver.chromium.org/downloads)** — необходим для работы Selenium.
- **[Poetry](https://python-poetry.org/docs/#installation)** — установка через официальную документацию.
- **[Docker](https://www.docker.com/get-started)** — инструкция по установке.


###  Автор
gewog  
📧 gewoggewog@gmail.com

### 📄 Лицензия
Проект распространяется под лицензией MIT.

<div align="center">
  <img src="https://media.tenor.com/NQtoHKskOY0AAAAi/cute-monster-monster.gif" alt="Demo of SmartAdBot" width="200" />
</div>