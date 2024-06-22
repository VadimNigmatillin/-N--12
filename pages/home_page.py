from base.base_page import BasePage
from config.links import Links
from config.locators import HomeLocators

class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    def navigate_to_login_page(self):
        
        self.page.click(HomeLocators.CLICK_SIGNUP_LOGIN)

    def navigate_to_login_pag_after_logout(self):
        
        self.page.click(HomeLocators.CLICK_LOGOUT)

    def navigate_to_contact_page(self):
        
        self.page.click(HomeLocators.CLICK_CONTACTUS)

    def navigate_to_products_page(self):
        
        self.page.click(HomeLocators.CLICK_PRODUCTS)

    def navigate_to_delete_page(self):
        
        self.page.click(HomeLocators.CLICK_DELETE)
    
    