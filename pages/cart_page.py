from pages.home_page import HomePage
from config.locators import CartViewLocators
from config.product_data import products

class CartView(HomePage):

    def check_product_visibility(self, product_id: int):
        product = self.page.locator(CartViewLocators.PRODUCT_ROW.format(product_id=product_id))
        return product.is_visible()
    
    def get_product_name(self, product_id: int) -> str:

        for product in products:
            if product.product_id == product_id:
                return product.name

    def get_product_price(self, product_id: int) -> str:

        for product in products:
            if product.product_id == product_id:
                return product.price
            

    def get_product_quantity(self, product_id: int) -> str:

        for product in products:
            if product.product_id == product_id:
                return product.quantity
            
    def get_product_total(self, product_id: int) -> str:

        for product in products:
            if product.product_id == product_id:
                return product.total

    