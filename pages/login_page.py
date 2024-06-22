from pages.home_page import HomePage
from config.locators import LogInLocators 

class LogIn(HomePage):

    def input_email(self, email):
        self.page.fill(LogInLocators.INPUT_EMAIL, email)

    def input_password(self, password):
        self.page.fill(LogInLocators.INPUT_PASSWORD, password)

    def click_login_button(self):
        self.page.click(LogInLocators.LOGIN_BUTTON)

    def login_heading_visibility(self):
        login_heading = self.page.locator(LogInLocators.LOGIN_HEADING)
        return login_heading.is_visible()

