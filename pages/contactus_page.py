from pages.home_page import HomePage
from config.locators import ContactUsLocators 
from playwright.sync_api import Page

class ContactUs(HomePage):

    def input_username(self, username):
        self.page.fill(ContactUsLocators.INPUT_USERNAME, username)

    def input_email(self, email):
        self.page.fill(ContactUsLocators.INPUT_EMAIL, email)

    def input_subject(self, subject):
        self.page.fill(ContactUsLocators.INPUT_SUBJECT, subject)

    def input_message(self, message):
        self.page.fill(ContactUsLocators.INPUT_MESSAGE, message)

    def input_file(self):
        self.page.click(ContactUsLocators.INPUT_FILE)

    def input_file(page: Page, file_input_locator, file_path):
        page.locator(file_input_locator).set_input_files(file_path)

    def click_submit(self):
        self.page.click(ContactUsLocators.INPUT_SUBMIT)
        
    def click_home(self):
        self.page.click(ContactUsLocators.CLICK_HOME)


    