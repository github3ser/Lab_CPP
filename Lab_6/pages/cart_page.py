from selenium.webdriver.common.by import By

class CartPage:
    FIRST_PRODUCT = (By.CLASS_NAME, "product-men")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".snipcart-details input[type='submit']")
    MINICART = (By.ID, "PPMiniCart")
    MINICART_ITEM_NAME = (By.CLASS_NAME, "minicart-name")
    MINICART_ITEM_PRICE = (By.CLASS_NAME, "minicart-price")
    MINICART_SUBTOTAL = (By.CLASS_NAME, "minicart-subtotal")
    MINICART_ITEM_QUANTITY = (By.CSS_SELECTOR, ".minicart-quantity")