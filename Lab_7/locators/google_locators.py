from selenium.webdriver.common.by import By

class GoogleLocators:
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.tF2Cxc")
    DID_YOU_MEAN_CONTAINER = (By.ID, "fprs")