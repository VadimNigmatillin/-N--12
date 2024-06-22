import allure
from config.links import Links
from utils import *

@allure.title("Тест API на получение списка брендов")
@allure.description("Этот тест проверяет корректность ответа API на запрос списка брендов.")
def test_brands_list_api(expected_brands_list):
    
    with allure.step("Отправка GET запроса к API"):
        response = send_get_request(Links.API_ALL_BRANDS_LIST)

    with allure.step("Проверка кода ответа"):
        check_response_code(response, 200)  

    with allure.step("Проверка формата ответа"):
        data = check_response_format(response)

    with allure.step("Проверка наличия ключа 'brands'"):
        check_json_key(data, 'brands')

    with allure.step("Проверка значения responseCode"):
        
        check_json_value(data, 'responseCode', 200)

    with allure.step("Сравнение полученных данных с ожидаемыми"):
        compare_json_data(data['brands'], expected_brands_list['brands'])
        