import allure
from utils import *
from config.links import Links

@allure.title("Тест создания и удаления аккаунта")
@allure.description("Этот тест отправляет запросы API для создания и удаления аккаунта пользователя.")
def test_create_and_delete_account(user_data, delete_payload):
    with allure.step("Отправка POST запроса к API для создания аккаунта"):
        create_response = send_post_request(Links.API_CREATE_ACCOUNT, user_data)

    with allure.step("Проверка кода ответа создания аккаунта"):
        check_response_code(create_response, 200) 

    with allure.step("Проверка значения responseCode в ответе на создание аккаунта"):
        create_data = create_response.json()
        check_json_key(create_data, 'responseCode')
        check_json_value(create_data, 'responseCode', 201)  

    with allure.step("Проверка сообщения об успешном создании аккаунта"):
        check_json_value(create_data, 'message', "User created!")

    with allure.step("Отправка DELETE запроса к API для удаления аккаунта"):
        delete_response = send_delete_request(Links.API_DELETE_ACCOUNT, delete_payload)

    with allure.step("Проверка кода ответа удаления аккаунта"):
        check_response_code(delete_response, 200)  

    with allure.step("Проверка значения responseCode в ответе на удаление аккаунта"):
        delete_data = delete_response.json()
        check_json_key(delete_data, 'responseCode')
        check_json_value(delete_data, 'responseCode', 200)  

    with allure.step("Проверка сообщения об успешном удалении аккаунта"):
        check_json_value(delete_data, 'message', "Account deleted!")

