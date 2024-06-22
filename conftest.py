import pytest
from playwright.sync_api import sync_playwright, BrowserContext
from config.user_data import user1
from tests.tests_api.utils import *
import json

# Фикстура для инициализации экземпляра Playwright
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p
# Открываем браузер Chrome
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(channel='chrome', headless=False)
    yield browser
    browser.close()

# Создаем новый контекст браузера с заданными параметрами
@pytest.fixture(scope="function")
def context(browser):
    context: BrowserContext = browser.new_context(viewport={"width": 1463, "height": 746})
    yield context
    context.close()

# Фикстура, предоставляющая данные пользователя
@pytest.fixture
def user_data():
    return {
        "name": user1.username,
        "email": user1.email,
        "password": user1.password,
        "title": user1.title,
        "birth_date": user1.birth_day,
        "birth_month": user1.birth_month,
        "birth_year": user1.birth_year,
        "firstname": user1.first_name,
        "lastname": user1.last_name,
        "company": user1.company,
        "address1": user1.address,
        "address2": user1.address2,
        "country": user1.country,
        "zipcode": user1.zipcode,
        "state": user1.state,
        "city": user1.city,
        "mobile_number": user1.phone
    }

# Фикстура для обновления данных пользователя
@pytest.fixture
def update_user_data():
    return {
        "name": "TestUpdate",
        "email": user1.email,
        "password": user1.password,
        "title": user1.title,
        "birth_date": user1.birth_day,
        "birth_month": user1.birth_month,
        "birth_year": user1.birth_year,
        "firstname": user1.first_name,
        "lastname": user1.last_name,
        "company": user1.company,
        "address1": user1.address,
        "address2": user1.address2,
        "country": user1.country,
        "zipcode": user1.zipcode,
        "state": user1.state,
        "city": user1.city,
        "mobile_number": user1.phone
    }

# Фикстура, предоставляющая данные для удаления пользователя
@pytest.fixture
def delete_payload(user_data):
    return {
        "email": user_data['email'],
        "password": user_data['password']
    }

# Фикстура для загрузки ожидаемого списка продуктов из JSON файла
@pytest.fixture
def expected_products_list():
    with open('config/all_products_list.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Фикстура для загрузки ожидаемого списка брендов из JSON файла 
@pytest.fixture
def expected_brands_list():
    with open('config/all_brands_list.json', 'r', encoding='utf-8') as file:
        return json.load(file)