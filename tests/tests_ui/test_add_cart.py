from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartView
from playwright.sync_api import Page, expect
from config.links import Links
from config.product_data import products
from config.locators import CartViewLocators, ProductsLocators
import allure

@allure.title("Тест добавления товаров в корзину")
@allure.description("Этот тест выполняет добавление товаров в коризину.")
def test_order_product(page: Page):

   
    with allure.step("Открытие домашней страницы"):
        home_page = HomePage(page)
        home_page.open_url()
        expect(page).to_have_url(Links.HOME_PAGE)

    
    with allure.step("Переход на страницу продуктов"):
        home_page.navigate_to_products_page()
        expect(page).to_have_url(Links.PRODUCTS_PAGE)

    products_page = ProductsPage(page)

   
    with allure.step("Проверка заголовка 'All Products'"):
        products_page.all_products_heading_visibility()
        expect(page.locator(ProductsLocators.ALL_PRODUCTS_HEADING)).to_be_visible()

   
    with allure.step("Добавление продуктов в корзину"):
        # Добавление первого продукта
        products_page.add_product(1)
        expect(page.locator(ProductsLocators.ADDED_MODAL_TITLE)).to_be_visible()
        products_page.contine_shopping()
        expect(page.locator(ProductsLocators.ADDED_MODAL_TITLE)).not_to_be_visible()
        
        # Добавление второго продукта
        products_page.add_product(2)
        expect(page.locator(ProductsLocators.ADDED_MODAL_TITLE)).to_be_visible()

    with allure.step("Переход на страницу корзины"):
        products_page.navigate_to_cart_page()
        expect(page).to_have_url(Links.CART_PAGE)

    cart_page = CartView(page)

    with allure.step("Проверка содержимого корзины"):
        for product in products:
            # Проверка наличия продукта по идентификатору
            cart_page.check_product_visibility(product.product_id)
            expect(page.locator(CartViewLocators.PRODUCT_ROW.format(product_id=product.product_id))).to_be_visible()

            # Проверка имени продукта
            actual_name = cart_page.get_product_name(product.product_id)
            locator = CartViewLocators.PRODUCT_DESCRIPTION.format(product_id=product.product_id, product_name=actual_name)
            element = page.locator(locator)
            expect(element).to_have_text(actual_name)

            # Проверка цены продукта
            actual_price = cart_page.get_product_price(product.product_id)
            locator = CartViewLocators.PRODUCT_PRICE.format(product_id=product.product_id, product_price=actual_price)
            element = page.locator(locator)
            expect(element).to_have_text(actual_price)

            # Проверка количества продукта
            actual_quantity = cart_page.get_product_quantity(product.product_id)
            locator = CartViewLocators.PRODUCT_QUANTITY.format(product_id=product.product_id, product_quantity=actual_quantity)
            element = page.locator(locator)
            expect(element).to_have_text(actual_quantity)

            # Проверка общей стоимости продукта
            actual_total = cart_page.get_product_total(product.product_id)
            locator = CartViewLocators.PRODUCT_TOTAL.format(product_id=product.product_id, product_total=actual_total)
            element = page.locator(locator)
            expect(element).to_have_text(actual_total)
