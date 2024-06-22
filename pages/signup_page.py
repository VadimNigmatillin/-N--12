from pages.home_page import HomePage
from config.locators import SignUpLocators 

class SignUp(HomePage):

    def input_username(self, username):
        self.page.fill(SignUpLocators.INPUT_USERNAME, username)

    def input_email(self, email):
        self.page.fill(SignUpLocators.INPUT_EMAIL, email)

    def click_signup_button(self):
        self.page.click(SignUpLocators.SIGNUP_BUTTON)

    def select_mr_mrs(self, title="Mr."):
        if title == "Mr.":
            self.page.click(SignUpLocators.RADIO_BTN_MR)
        elif title == "Mrs.":
            self.page.click(SignUpLocators.RADIO_BTN_MRS)

    def input_password(self, password):
        self.page.fill(SignUpLocators.INPUT_PASSWORD, password)

    def select_date_of_birth(self, year, month, day):
        self.page.select_option(SignUpLocators.SELECT_BIRTH_YEAR, year)
        self.page.select_option(SignUpLocators.SELECT_BIRTH_MONTH, month)
        self.page.select_option(SignUpLocators.SELECT_BIRTH_DAY, day)

    def click_checkbox_newsletter(self):
        self.page.check(SignUpLocators.CHECKBOX_NEWSLETTER)

    def click_checkbox_offer(self):
        self.page.check(SignUpLocators.CHECKBOX_SPECIAL_OFFERS)

    def input_first_name(self, first_name):
        self.page.fill(SignUpLocators.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name):
        self.page.fill(SignUpLocators.INPUT_LAST_NAME, last_name)

    def input_company(self, company):
        self.page.fill(SignUpLocators.INPUT_COMPANY, company)

    def input_address(self, address):
        self.page.fill(SignUpLocators.INPUT_ADDRESS, address)
    
    def input_address_2(self, address2):
        self.page.fill(SignUpLocators.INPUT_ADDRESS_2, address2)

    def select_country(self, country):
        self.page.select_option(SignUpLocators.SELECT_COUNTRY, country)  

    def input_state(self, state):
        self.page.fill(SignUpLocators.INPUT_STATE, state)

    def input_city(self, city):
        self.page.fill(SignUpLocators.INPUT_CITY, city)

    def input_zipcode(self, zipcode):
        self.page.fill(SignUpLocators.INPUT_ZIPCODE, zipcode)

    def input_phone(self, phone):
        self.page.fill(SignUpLocators.INPUT_MOBILE_NUMBER, phone)
    
    def click_create_account_button(self):
        self.page.click(SignUpLocators.CREATE_ACCOUNT_BUTTON)

    def input_sub_email(self, sub_email):
            self.page.fill(SignUpLocators.INPUT_SUBSCRIPTION_EMAIL, sub_email)

    def click_button_sub_email(self):
        self.page.click(SignUpLocators.BUTTON_SUBSCRIPTION_EMAIL)
        self.page.wait_for_selector(SignUpLocators.ALERT_SUCCESS_MESSAGE)

    def signup_heading_visibility(self):
        signup_heading = self.page.locator(SignUpLocators.SIGNUP_HEADING)
        return signup_heading.is_visible()
    
    def click_contine_button(self):
        self.page.click(SignUpLocators.CONTINE_BUTTON)
