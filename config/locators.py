class AgreementLocators:
    AGREEMENT_BUTTON = 'p.fc-button-label:text("Соглашаюсь")'

class SignUpLocators:
    INPUT_USERNAME = "//input[@name='name']"
    INPUT_EMAIL = "//input[@data-qa='signup-email']"
    SIGNUP_BUTTON = "//button[@data-qa='signup-button']"
    RADIO_BTN_MR = "//div[@id='uniform-id_gender1']"
    RADIO_BTN_MRS = "//div[@id='uniform-id_gender2']"
    INPUT_PASSWORD = "//input[@data-qa='password']"
    SELECT_BIRTH_YEAR = "//select[@data-qa='years']"
    SELECT_BIRTH_MONTH = "//select[@data-qa='months']"
    SELECT_BIRTH_DAY = "//select[@data-qa='days']"
    CHECKBOX_NEWSLETTER = "//input[@id='newsletter']"
    CHECKBOX_SPECIAL_OFFERS = "//input[@id='optin']"
    INPUT_FIRST_NAME = "//input[@data-qa='first_name']"
    INPUT_LAST_NAME = "//input[@data-qa='last_name']"
    INPUT_COMPANY = "//input[@data-qa='company']"
    INPUT_ADDRESS = "//input[@data-qa='address']"
    INPUT_ADDRESS_2 = "//input[@data-qa='address2']"
    SELECT_COUNTRY = "//select[@data-qa='country']"
    INPUT_STATE = "//input[@data-qa='state']"
    INPUT_CITY = "//input[@data-qa='city']"
    INPUT_ZIPCODE = "//input[@data-qa='zipcode']"
    INPUT_MOBILE_NUMBER = "//input[@data-qa='mobile_number']" 
    CREATE_ACCOUNT_BUTTON = "//button[@data-qa='create-account']"
    ACCOUNT_CREATED = "text='Account Created!'"
    INPUT_SUBSCRIPTION_EMAIL = "//input[@id='susbscribe_email']"
    BUTTON_SUBSCRIPTION_EMAIL = "//button[@id='subscribe']"
    ALERT_SUCCESS_MESSAGE = "//div[@class='alert-success alert']"
    SIGNUP_HEADING = "h2:has-text('Login to your account')"
    CONTINE_BUTTON = "//a[@data-qa='continue-button']"
    ACCOUNT_DELETED = "text='Account Deleted!'"


class LogInLocators:
    INPUT_EMAIL = "//input[@data-qa='login-email']"
    INPUT_PASSWORD = "//input[@data-qa='login-password']"
    LOGIN_BUTTON = "//button[@data-qa='login-button']"
    LOGIN_HEADING = "h2:has-text('Login to your account')"
    
class ContactUsLocators:
    INPUT_USERNAME = "//input[@data-qa='name']"
    INPUT_EMAIL = "//input[@data-qa='email']"
    INPUT_SUBJECT = "//input[@data-qa='subject']"
    INPUT_MESSAGE = "//textarea[@data-qa='message']"
    INPUT_FILE = "//input[@type='file']"
    INPUT_SUBMIT = "//input[@data-qa='submit-button']"
    ALERT_SUCCESS = "//div[@class='status alert alert-success']"
    CLICK_HOME = "//i[@class='fa fa-angle-double-left']"


class HomeLocators:
    CLICK_SIGNUP_LOGIN = "text=' Signup / Login'"
    CLICK_LOGOUT = "text=' Logout'"
    CLICK_CONTACTUS = "text=' Contact us'"
    CLICK_PRODUCTS = "text=' Products'"
    CLICK_DELETE = "text=' Delete Account'"
    
    



    @staticmethod
    def user_locator(username: str) -> str:
        return f"b:text('{username}')"


class ProductsLocators:
    INPUT_SEARCH_PRODUCTS = "//input[@id='search_product']"
    BUTTON_SEARCH = "//button[@id='submit_search']"
    ALL_PRODUCTS_HEADING = "h2:has-text('All Products')"
    SEARCHED_PRODUCTS_HEADING = "h2:has-text('Searched Products')"
    PRODUCT_CARDS = "//div[@class='productinfo text-center']"
    PRODUCT_NAME = "p"
    ADD_PRODUCT_BUTTON = "//a[@data-product-id='{product_id}']"
    ADDED_MODAL_TITLE = "h4:has-text('Added!')"
    CONTINUE_SHOPPING_BUTTON = "button:has-text('Continue Shopping')"
    CLICK_VIEW_CARD = "text='View Cart'"
    
class CartViewLocators:
    PRODUCT_ROW = "//tr[@id='product-{product_id}']"
    PRODUCT_DESCRIPTION = "//tr[@id='product-{product_id}']//td[@class='cart_description']//h4/a[text()='{product_name}']"
    PRODUCT_PRICE = "//tr[@id='product-{product_id}']//td[@class='cart_price']//p[text()='{product_price}']"
    PRODUCT_QUANTITY = "//tr[@id='product-{product_id}']//td[@class='cart_quantity']//button[text()='{product_quantity}']"
    PRODUCT_TOTAL = "//tr[@id='product-{product_id}']//td[@class='cart_total']//p[text()='{product_total}']"








  


    
