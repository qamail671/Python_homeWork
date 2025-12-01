# Python_homeWork
# Автоматизация тестирования интернет-магазина

Проект использует **pytest**, **Selenium WebDriver** и **Allure Report** для автоматизации UI-тестов интернет-магазина [www.saucedemo.com](https://www.saucedemo.com).
Тесты проверяют полный сценарий покупки товаров.

## 🚀 Быстрый старт

### 1. Установка зависимостей

# Автоматизация тестирования интернет-магазина

Проект использует **pytest**, **Selenium WebDriver** и **Allure Report** для автоматизации UI-тестов интернет-магазина.
Тесты проверяют полный сценарий покупки товаров.
# 1. Установка зависимостей
pip install -r requirements.txt


### 2. Установка Allure
- Скачайте [Allure](https://github.com/allure-framework/allure2/releases)
- Добавьте `bin/allure` в PATH
- Проверьте: `allure --version`

## 🧪 Запуск тестов

### Базовый запуск
pytest test_shop.py -v -s


### С генерацией Allure отчета
pytest test_shop.py --alluredir=allure-results -v -s

Результаты сохраняются в папку `allure-results` [web:21][web:22][file:18].

## 📊 Просмотр отчета Allure

### Автоматическое открытие в браузере
allure serve allure-results

text
Отчет откроется на `http://localhost:5000` [web:21][web:25][web:30].

### Генерация статического отчета
allure generate allure-results -o allure-report --clean
allure open allure-report

text
Отчет сохранится в папку `allure-report` [web:23].

## Структура проекта

├── test_shop.py # корзина
├── cart_page.py # карта
├── checkout_page.py # магазин
├── loginpage.py # логинация
├── mainpage.py #  главная страница
└── requirements.txt