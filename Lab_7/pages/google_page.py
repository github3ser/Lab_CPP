from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.google_locators import GoogleLocators

class GooglePage(BasePage):
    def open_home(self):
        self.driver.get("https://www.google.co.in")

    def type_search(self, text):
        search_box = self.find(GoogleLocators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(text)

    def search_enter(self):
        self.find(GoogleLocators.SEARCH_BOX).submit()

    def click_search_button(self):
        # Folosește doar elementul vizibil și activ
        buttons = self.driver.find_elements(*GoogleLocators.SEARCH_BUTTON)
        for btn in buttons:
            if btn.is_displayed() and btn.is_enabled():
                btn.click()
                return

    def get_results(self):
        return self.finds(GoogleLocators.SEARCH_RESULTS)

    def has_did_you_mean(self, timeout=5):
        try:
            suggestion = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(GoogleLocators.DID_YOU_MEAN_CONTAINER)
            )
            return "Vezi rezultate pentru" in suggestion.text
        except:
            return False
