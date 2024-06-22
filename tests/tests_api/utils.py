import requests
import pytest

def send_put_request(url,payload):
    response = requests.put(url,data=payload)
    check_response_format(response)
    return response

def send_get_request(url):
    response = requests.get(url)
    check_response_format(response)
    return response

def send_post_request(url, payload):
    response = requests.post(url, data=payload)
    check_response_format(response)
    return response

def send_delete_request(url, payload):
    response = requests.delete(url, data=payload)
    check_response_format(response)
    return response

def check_response_format(response):
    try:
        response_data = response.json()
    except ValueError:
        pytest.fail(f"Ответ не в формате JSON: {response.text}")
    return response_data

def check_response_code(response, expected_code):
    assert response.status_code == expected_code, f"Ожидался код ответа {expected_code}, но получен {response.status_code}"

def check_json_key(response_json, key):
    assert key in response_json, f"Ключ '{key}' не найден в JSON ответе"

def check_json_value(response_json, key, expected_value):
    assert response_json[key] == expected_value, f"Ожидалось значение '{expected_value}' для ключа '{key}', но получено {response_json[key]}"

def compare_json_data(actual_data, expected_data):
    assert actual_data == expected_data, "Полученные данные JSON не соответствуют ожидаемым данным"

def check_product_structure(product):
    expected_product_keys = {'id', 'name', 'price', 'brand', 'category'}
    expected_category_keys = {'usertype', 'category'}
    expected_usertype_keys = {'usertype'}

    # Проверка, что все ожидаемые ключи присутствуют в продукте
    assert all(key in product for key in expected_product_keys), f"Продукт не содержит одного из ожидаемых ключей: {expected_product_keys}"

    # Проверка структуры ключа 'category'
    category = product['category']
    assert all(key in category for key in expected_category_keys), f"Категория не содержит одного из ожидаемых ключей: {expected_category_keys}"

    # Проверка структуры ключа 'usertype' внутри 'category'
    usertype = category['usertype']
    assert all(key in usertype for key in expected_usertype_keys), f"Тип пользователя не содержит одного из ожидаемых ключей: {expected_usertype_keys}"

    # Дополнительные проверки значений
    assert isinstance(product['id'], int), "Значение 'id' должно быть целым числом"
    assert isinstance(product['name'], str), "Значение 'name' должно быть строкой"
    assert isinstance(product['price'], str), "Значение 'price' должно быть строкой"
    assert isinstance(product['brand'], str), "Значение 'brand' должно быть строкой"
    assert isinstance(category['category'], str), "Значение 'category' должно быть строкой"
    assert isinstance(usertype['usertype'], str), "Значение 'usertype' должно быть строкой"