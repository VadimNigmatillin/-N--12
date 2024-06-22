from pages.home_page import HomePage
from config.locators import ProductsLocators


class ProductsPage(HomePage):

    def all_products_heading_visibility(self):
        all_products_heading = self.page.locator(ProductsLocators.ALL_PRODUCTS_HEADING)
        return all_products_heading.is_visible()
    
    def input_products(self, product):
        self.page.fill(ProductsLocators.INPUT_SEARCH_PRODUCTS, product)

    def click_search_button(self):
        self.page.click(ProductsLocators.BUTTON_SEARCH)

    def searched_products_heading_visibility(self):
        searched_products_heading = self.page.locator(ProductsLocators.SEARCHED_PRODUCTS_HEADING)
        return searched_products_heading.is_visible()
    
    def add_product(self, product_id):
        
        self.page.click(ProductsLocators.ADD_PRODUCT_BUTTON.format(product_id=product_id))

    def navigate_to_cart_page(self):
        
        self.page.click(ProductsLocators.CLICK_VIEW_CARD)

    def contine_shopping(self):

        self.page.click(ProductsLocators.CONTINUE_SHOPPING_BUTTON)


    def add_product(self, product_id):
        
        self.page.click(ProductsLocators.ADD_PRODUCT_BUTTON.format(product_id=product_id))

    def navigate_to_cart_page(self):
            
        self.page.click(ProductsLocators.CLICK_VIEW_CARD)

    def contine_shopping(self):

        self.page.click(ProductsLocators.CONTINUE_SHOPPING_BUTTON)

        

    