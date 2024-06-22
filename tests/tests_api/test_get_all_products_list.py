import allure
from config.links import Links
from utils import *

@allure.title("Тест API на получение списка продуктов")
@allure.description("Этот тест проверяет корректность ответа API на запрос списка продуктов.")
def test_api_products_list(expected_products_list):

    with allure.step("Отправка GET запроса к API"):
        response = send_get_request(Links.API_GET_ALL_PRODUCTS_LIST)

    with allure.step("Проверка кода ответа"):
        check_response_code(response, 200)  

    with allure.step("Проверка формата ответа"):
        data = check_response_format(response)

    with allure.step("Проверка наличия ключа 'products'"):
        check_json_key(data, 'products')

    with allure.step("Проверка значения responseCode"):
        check_json_value(data, 'responseCode', 200)

    with allure.step("Сравнение полученных данных с ожидаемыми"):
        
        compare_json_data(data, expected_products_list)
