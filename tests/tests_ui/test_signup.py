import os
from pages.home_page import HomePage
from pages.signup_page import SignUp
from playwright.sync_api import Page, expect
from config.user_data import user1
from config.links import Links
from config.locators import SignUpLocators
import allure

@allure.title("Тест регистрации нового пользователя")
@allure.description("Этот тест выполняет регистрацию нового пользователя с валидными данными и проверяет успешность создания аккаунта.")
def test_signup(page: Page):

   
    with allure.step("Открытие домашней страницы"):
        home_page = HomePage(page)
        home_page.open_url()
        expect(page).to_have_url(Links.HOME_PAGE)

   
    with allure.step("Переход на страницу входа/регистрации"):
        home_page.navigate_to_login_page()
        expect(page).to_have_url(Links.LOGIN_PAGE)

    signup_page = SignUp(page)
    
   
    with allure.step("Проверка заголовка 'Sign up to your account'"):
        signup_page.signup_heading_visibility()
        expect(page.locator(SignUpLocators.SIGNUP_HEADING)).to_be_visible()

   
    with allure.step("Ввод имени пользователя"):
        signup_page.input_username(user1.username)
        expect(page.locator(SignUpLocators.INPUT_USERNAME)).to_have_value(user1.username)
    
   
    with allure.step("Ввод email"):
        signup_page.input_email(user1.email)
        expect(page.locator(SignUpLocators.INPUT_EMAIL)).to_have_value(user1.email)
    
    
    with allure.step("Нажатие на кнопку регистрации"):
        with page.expect_navigation():
            signup_page.click_signup_button()
    
   
    with allure.step("Проверка URL новой страницы"):
        expect(page).to_have_url(Links.SIGNUP_PAGE)
    
   
    with allure.step("Выбор пола"):
        signup_page.select_mr_mrs(user1.title)
        if user1.title == "Mr.":
            expect(page.locator(SignUpLocators.RADIO_BTN_MR)).to_be_checked()
        elif user1.title == "Mrs.":
            expect(page.locator(SignUpLocators.RADIO_BTN_MRS)).to_be_checked()
    
   
    with allure.step("Ввод пароля"):
        signup_page.input_password(user1.password)
        expect(page.locator(SignUpLocators.INPUT_PASSWORD)).to_have_value(user1.password)
    
   
    with allure.step("Выбор даты рождения"):
        signup_page.select_date_of_birth(user1.birth_year, user1.birth_month, user1.birth_day)
        expect(page.locator(SignUpLocators.SELECT_BIRTH_YEAR)).to_have_value(user1.birth_year)
        expect(page.locator(SignUpLocators.SELECT_BIRTH_MONTH)).to_have_value(user1.birth_month)
        expect(page.locator(SignUpLocators.SELECT_BIRTH_DAY)).to_have_value(user1.birth_day)
    
   
    with allure.step("Нажатие чекбокса для подписки на рассылку новостей"):
        signup_page.click_checkbox_newsletter()
        expect(page.locator(SignUpLocators.CHECKBOX_NEWSLETTER)).to_be_checked()
    
    
    with allure.step("Нажатие чекбокса для специальных предложений"):
        signup_page.click_checkbox_offer()
        expect(page.locator(SignUpLocators.CHECKBOX_SPECIAL_OFFERS)).to_be_checked()
    
    
    with allure.step("Ввод имени"):
        signup_page.input_first_name(user1.first_name)
        expect(page.locator(SignUpLocators.INPUT_FIRST_NAME)).to_have_value(user1.first_name)
    
    
    with allure.step("Ввод фамилии"):
        signup_page.input_last_name(user1.last_name)
        expect(page.locator(SignUpLocators.INPUT_LAST_NAME)).to_have_value(user1.last_name)
    
    
    with allure.step("Ввод названия компании"):
        signup_page.input_company(user1.company)
        expect(page.locator(SignUpLocators.INPUT_COMPANY)).to_have_value(user1.company)
    
    
    with allure.step("Ввод адреса"):
        signup_page.input_address(user1.address)
        expect(page.locator(SignUpLocators.INPUT_ADDRESS)).to_have_value(user1.address)
    
    
    with allure.step("Ввод дополнительного адреса"):
        signup_page.input_address_2(user1.address2)
        expect(page.locator(SignUpLocators.INPUT_ADDRESS_2)).to_have_value(user1.address2)
    
    
    with allure.step("Выбор страны"):
        signup_page.select_country(user1.country)
        expect(page.locator(SignUpLocators.SELECT_COUNTRY)).to_have_value(user1.country)
    
    
    with allure.step("Ввод штата/области"):
        signup_page.input_state(user1.state)
        expect(page.locator(SignUpLocators.INPUT_STATE)).to_have_value(user1.state)
    
    
    with allure.step("Ввод города"):
        signup_page.input_city(user1.city)
        expect(page.locator(SignUpLocators.INPUT_CITY)).to_have_value(user1.city)
    
    
    with allure.step("Ввод почтового индекса"):
        signup_page.input_zipcode(user1.zipcode)
        expect(page.locator(SignUpLocators.INPUT_ZIPCODE)).to_have_value(user1.zipcode)
    
    
    with allure.step("Ввод номера телефона"):
        signup_page.input_phone(user1.phone)
        expect(page.locator(SignUpLocators.INPUT_MOBILE_NUMBER)).to_have_value(user1.phone)

    
    with allure.step("Ввод дополнительного email для подписки"):
        signup_page.input_sub_email(user1.sub_email)
        expect(page.locator(SignUpLocators.INPUT_SUBSCRIPTION_EMAIL)).to_have_value(user1.sub_email)

    
    with allure.step("Нажатие на кнопку для подписки дополнительного email"):
        signup_page.click_button_sub_email()
        expect(page.locator(SignUpLocators.ALERT_SUCCESS_MESSAGE)).to_be_visible()

    
    with allure.step("Нажатие на кнопку завершения регистрации"):
        with page.expect_navigation():
            signup_page.click_create_account_button()
    
    
    with allure.step("Проверка URL страницы после успешной регистрации"):
        expect(page).to_have_url(Links.ACCOUNT_CREATED_PAGE)
    
    
    with allure.step("Проверка наличия подтверждающего элемента на странице"):
        expect(page.locator(SignUpLocators.ACCOUNT_CREATED)).to_be_visible()

   
    with allure.step("Переход на домашнюю страницу после регистрации"):
        signup_page.click_contine_button()
        expect(page).to_have_url(Links.HOME_PAGE)

    
    with allure.step("Нажатие на кнопку удалить аккаунт"):
        home_page.navigate_to_delete_page()
        expect(page).to_have_url(Links.DELETE_PAGE)

    
    with allure.step("Проверка удаленного аккаунта"):
        expect(page.locator(SignUpLocators.ACCOUNT_DELETED)).to_be_visible()
    

    #page.wait_for_timeout(10000)
