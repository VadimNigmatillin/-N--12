import pytest
import allure
from config.links import Links
from utils import *

@allure.title("API тест поиска продукта")
@allure.description("Этот тест проверяет поиск продуктов через API и проверяет структуру возвращаемых данных.")
@pytest.mark.parametrize("search_term", ["Blue top"])
def test_search_product_api(search_term):

    
    with allure.step(f"Отправка POST запроса к API для поиска продукта: '{search_term}'"):
        payload = {"search_product": search_term}
        response = send_post_request(Links.API_SEARCH, payload)

    
    with allure.step("Проверка кода ответа"):
        check_response_code(response, 200)

    with allure.step("Проверка формата ответа"):
        data = check_response_format(response)

   
    with allure.step("Проверка наличия ключа 'products' в JSON ответе"):
        check_json_key(data, 'products')

   
    with allure.step("Проверка значения responseCode в JSON ответе"):
        check_json_value(data, 'responseCode', 200)

    
    with allure.step("Проверка структуры каждого продукта в JSON ответе"):
        for product in data['products']:
            check_product_structure(product)
