# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем Poetry
RUN pip install --upgrade pip && \
    pip install poetry==2.2.0

# Устанавливаем зависимости для работы с браузером
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -O /tmp/chrome.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/124.0.6367.91/linux64/chrome-linux64.zip && \
    unzip /tmp/chrome.zip -d /opt && \
    rm /tmp/chrome.zip && \
    mv /opt/chrome-linux64 /opt/chrome && \
    ln -s /opt/chrome/chrome /usr/bin/google-chrome && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

# Копируем остальные файлы проекта
COPY . .

# Запускаем основной скрипт
CMD ["poetry", "run", "python", "main.py"]
