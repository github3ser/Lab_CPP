from selenium.webdriver.common.by import By

class ProductPage:
    PRODUCT_ITEMS = (By.CLASS_NAME, "product-men")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h4 > a")
    PRODUCT_PRICE = (By.CLASS_NAME, "item_price")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.link-product-add-cart")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")  # dacă există pagina de eroare