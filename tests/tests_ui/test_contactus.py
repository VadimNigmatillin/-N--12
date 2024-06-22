import os
from pages.home_page import HomePage
from pages.contactus_page import ContactUs
from playwright.sync_api import Page, expect
from config.message_data import message1
from config.links import Links
from config.locators import ContactUsLocators
import allure

@allure.title("Тест страницы 'Contact Us'")
@allure.description("Этот тест заполняет форму на странице 'Contact Us' с валидными данными и проверяет успешность отправки сообщения.")
def test_contactus(page: Page):

    
    with allure.step("Открытие домашней страницы"):
        home_page = HomePage(page)
        home_page.open_url()
        expect(page).to_have_url(Links.HOME_PAGE)

    
    with allure.step("Переход на страницу 'Contact Us'"):
        home_page.navigate_to_contact_page()
        expect(page).to_have_url(Links.CONTACTUS_PAGE)

    contact_page = ContactUs(page)

    
    with allure.step("Заполнение поля имени пользователя"):
        contact_page.input_username(message1.username)
        expect(page.locator(ContactUsLocators.INPUT_USERNAME)).to_have_value(message1.username)

    
    with allure.step("Заполнение поля email"):
        contact_page.input_email(message1.email)
        expect(page.locator(ContactUsLocators.INPUT_EMAIL)).to_have_value(message1.email)

   
    with allure.step("Заполнение поля темы сообщения"):
        contact_page.input_subject(message1.subject)
        expect(page.locator(ContactUsLocators.INPUT_SUBJECT)).to_have_value(message1.subject)

   
    with allure.step("Заполнение поля сообщения"):
        contact_page.input_message(message1.message)
        expect(page.locator(ContactUsLocators.INPUT_MESSAGE)).to_have_value(message1.message)

   
    with allure.step("Загрузка файла"):
        ContactUs.input_file(page, ContactUsLocators.INPUT_FILE, message1.file_path)
        file_name = os.path.basename(message1.file_path)
        expect(page.locator(ContactUsLocators.INPUT_FILE)).to_have_value(f'C:\\fakepath\\{file_name}')

    
    with allure.step("Отправка формы и проверка успешности"):
        page.on('dialog', lambda dialog: dialog.accept())
        page.wait_for_timeout(1000)
        contact_page.click_submit()
        expect(page.locator(ContactUsLocators.ALERT_SUCCESS)).to_be_visible()

    
    
    with allure.step("Переход на домашнюю страницу"):
        contact_page.click_home()
        expect(page).to_have_url(Links.HOME_PAGE)
    
    #page.wait_for_timeout(10000)
