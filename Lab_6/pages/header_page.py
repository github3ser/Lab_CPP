from selenium.webdriver.common.by import By

class HeaderPage:

    # Toate itemele principale din meniu
    MENU_ITEMS = (By.CSS_SELECTOR, "ul.menu__list > li > a.menu__link")

    # Iteme simple
    HOME_LINK = (By.CSS_SELECTOR, "a.menu__link[href='/']")
    ABOUT_LINK = (By.CSS_SELECTOR, "a.menu__link[href='/about']")
    CONTACT_LINK = (By.CSS_SELECTOR, "a.menu__link[href='/contact']")

    # Dropdown – Men's wear
    MEN_DROPDOWN = (By.CSS_SELECTOR, "li.dropdown.menu__item:nth-child(3) > a.menu__link")
    MEN_CLOTHING = (By.CSS_SELECTOR, "a[href='/mens']")
    MEN_ACCESSORIES = (By.CSS_SELECTOR, "a[href='/mens2']")

    # Dropdown – Women's wear
    WOMEN_DROPDOWN = (By.CSS_SELECTOR, "li.dropdown.menu__item:nth-child(4) > a.menu__link")
    WOMEN_CLOTHING = (By.CSS_SELECTOR, "a[href='/womens']")
    WOMEN_ACCESSORIES = (By.CSS_SELECTOR, "a[href='/womens2']")
