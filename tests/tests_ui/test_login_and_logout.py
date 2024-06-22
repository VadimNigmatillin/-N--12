from pages.home_page import HomePage
from pages.login_page import LogIn
from playwright.sync_api import Page, expect
from config.user_data import user1
from config.links import Links
from config.locators import HomeLocators, LogInLocators
import allure
from tests.tests_api.utils import*

@allure.title("Тест входа и выхода")
@allure.description("Этот тест выполняет вход с валидными учетными данными, проверяет имя пользователя и выходит из аккаунта.")
def test_login_and_logout(page: Page, user_data, delete_payload ):

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

   
    with allure.step("Открытие домашней страницы"):
        home_page = HomePage(page)
        home_page.open_url()
        expect(page).to_have_url(Links.HOME_PAGE)


    
    with allure.step("Переход на страницу входа"):
        home_page.navigate_to_login_page()
        expect(page).to_have_url(Links.LOGIN_PAGE)

    login_page = LogIn(page)

    
    with allure.step("Проверка заголовка 'Login to your account'"):
        login_page.login_heading_visibility()
        expect(page.locator(LogInLocators.LOGIN_HEADING)).to_be_visible()

   
    with allure.step("Ввод email"):
        login_page.input_email(user1.email)
        expect(page.locator(LogInLocators.INPUT_EMAIL)).to_have_value(user1.email)

    
    with allure.step("Ввод пароля"):
        login_page.input_password(user1.password)
        expect(page.locator(LogInLocators.INPUT_PASSWORD)).to_have_value(user1.password)

    
    with allure.step("Нажатие на кнопку Login и переход на домашнюю страницу"):
        with page.expect_navigation():
            login_page.click_login_button()
        expect(page).to_have_url(Links.HOME_PAGE)

    
    with allure.step("Проверка имени пользователя на домашней странице"):
        expect(page.locator(HomeLocators.user_locator(user1.username))).to_have_text(user1.username)

   
    with allure.step("Выход из аккаунта и переход на страницу входа"):
        home_page.navigate_to_login_pag_after_logout()
        expect(page).to_have_url(Links.LOGIN_PAGE)

    
    with allure.step("Повторная проверка заголовка 'Login to your account'"):
        login_page.login_heading_visibility()
        expect(page.locator(LogInLocators.LOGIN_HEADING)).to_be_visible()

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
