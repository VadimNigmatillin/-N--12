from config.locators import AgreementLocators
class BasePage:
    PAGE_URL = None
    def __init__(self, page):
        self.page = page

    def open_url(self):
        if self.PAGE_URL:
            self.page.goto(self.PAGE_URL)
        else:
            print('Нельзя открыть без PAGE_URL')
        if self.page.locator(AgreementLocators.AGREEMENT_BUTTON).is_visible():
            self.page.locator(AgreementLocators.AGREEMENT_BUTTON).click()
        