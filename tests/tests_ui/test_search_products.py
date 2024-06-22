from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect
from config.links import Links
from config.locators import ProductsLocators
import allure

@allure.title("Тест поиска продуктов")
@allure.description("Этот тест проверяет функционал поиска продуктов на странице каталога.")


def test_search_products(page: Page):
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

    # Задаем поисковый запрос
    search_term = "Blue"


    
    with allure.step(f"Ввод текста для поиска: '{search_term}'"):
        
        products_page.input_products(search_term)
        expect(page.locator(ProductsLocators.INPUT_SEARCH_PRODUCTS)).to_have_value(search_term)

    
    with allure.step("Нажатие кнопки поиска"):
        products_page.click_search_button()
        expect(page).to_have_url(f"{Links.PRODUCTS_PAGE}?search={search_term.replace(' ', '%20')}")

   
    with allure.step("Проверка заголовка 'Searched Products'"):
        products_page.searched_products_heading_visibility()
        expect(page.locator(ProductsLocators.SEARCHED_PRODUCTS_HEADING)).to_be_visible()

    
    with allure.step(f"Проверка, что все продукты содержат введенное значение: '{search_term}'"):
        product_cards = page.locator(ProductsLocators.PRODUCT_CARDS)
        count = product_cards.count()

        # Проверяем, что название каждого найденного продукта содержит поисковый запрос
        for i in range(count):
            product_name_locator = product_cards.nth(i).locator(ProductsLocators.PRODUCT_NAME)
            product_name = product_name_locator.text_content().strip().lower()
            assert search_term.lower() in product_name, \
                f"Название продукта '{product_name}' не содержит поисковый запрос '{search_term.lower()}'"
