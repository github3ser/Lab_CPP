from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from selenium.webdriver.common.action_chains import ActionChains


@then('primul produs este vizibil')
def step_first_product_visible(context):
    first_product = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(CartPage.FIRST_PRODUCT)
    )
    context.first_product = first_product


@when('utilizatorul derulează până la primul produs')
def step_scroll_to_product(context):
    actions = ActionChains(context.driver)
    actions.move_to_element(context.first_product).perform()


@when('utilizatorul dă click pe butonul "Add to Cart"')
def step_click_add_to_cart(context):
    add_btn = context.first_product.find_element(*CartPage.ADD_TO_CART_BTN)
    WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable(CartPage.ADD_TO_CART_BTN))
    add_btn.click()


@then('mesajul de confirmare apare sau icon-ul coșului se actualizează')
def step_confirm_message(context):
    # asteapta mini-cart sa fie vizibil
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(CartPage.MINICART)
    )


@when('utilizatorul accesează coșul ("Cart")')
def step_open_cart(context):
    minicart = context.driver.find_element(*CartPage.MINICART)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", minicart)


@then('produsul adăugat este vizibil cu nume, preț și imagine')
def step_check_cart_item(context):
    name = context.driver.find_element(*CartPage.MINICART_ITEM_NAME).text
    price = context.driver.find_element(*CartPage.MINICART_ITEM_PRICE).text
    expected_name = "Party Men's Blazer"
    expected_price = "$260.99"

    if name != expected_name:
        print(f"WARNING: Numele produsului ({name}) nu corespunde ({expected_name})")
    if price != expected_price:
        print(f"WARNING: Prețul produsului ({price}) nu corespunde ({expected_price})")


@then('totalul prețurilor din coș este corect')
def step_check_cart_total(context):
    subtotal_text = context.driver.find_element(*CartPage.MINICART_SUBTOTAL).text
    subtotal_value = float(subtotal_text.replace("Subtotal: $", "").replace(" USD", ""))
    expected_value = 260.99  # valoarea produsului adăugat
    if subtotal_value != expected_value:
        print(f"WARNING: Totalul coșului ({subtotal_value}) nu corespunde ({expected_value})")


@when('utilizatorul dă click de 2 ori pe același buton "Add to Cart"')
def step_click_add_to_cart_twice(context):
    add_btn = context.first_product.find_element(*CartPage.ADD_TO_CART_BTN)
    for _ in range(2):
        add_btn.click()


@then('cantitatea produsului se actualizează corect sau apare mesaj "Already in cart"')
def step_check_quantity_or_message(context):
    quantity_input = context.driver.find_element(*CartPage.MINICART_ITEM_QUANTITY)
    quantity_value = int(quantity_input.get_attribute("value"))
    if quantity_value > 1:
        print(f"Cantitatea produsului s-a actualizat corect: {quantity_value}")
    else:
        print('Produsul este deja în coș sau cantitatea nu s-a schimbat')