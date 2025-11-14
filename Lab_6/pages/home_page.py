from selenium.webdriver.common.by import By

class HomePage:
    HEADER = (By.TAG_NAME, "header")
    NAV_LINKS = (By.CSS_SELECTOR, "header a")
    PRODUCT_ITEMS = (By.CLASS_NAME, "product-men")
    FOOTER = (By.CLASS_NAME, "footer")