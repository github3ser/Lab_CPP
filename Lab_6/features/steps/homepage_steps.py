from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage

@then('pagina se încarcă complet fără erori')
def step_page_loaded(context):
    state = context.driver.execute_script("return document.readyState")
    assert state == "complete", f"Pagina nu s-a încărcat complet (readyState={state})"

@then('header-ul și meniul sunt vizibile')
def step_header_and_menu(context):
    # Așteaptă până când div-ul cu clasa "header" devine vizibil
    header = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "header"))
    )

    # Caută toate linkurile din interiorul header-ului
    nav_links = context.driver.find_elements(By.CSS_SELECTOR, ".header a")

    assert header.is_displayed(), "Header-ul nu este vizibil."
    assert len(nav_links) > 0, "Nu s-au găsit linkuri în meniu."

@then('sunt afișate cel puțin 3 produse')
def step_products(context):
    products = context.driver.find_elements(*HomePage.PRODUCT_ITEMS)
    print("Produse găsite:", len(products))
    assert len(products) >= 3, f"S-au găsit doar {len(products)} produse"

@then('footer-ul conține linkul "Contact"')
def step_footer(context):
    footer = context.driver.find_element(*HomePage.FOOTER)
    assert "Contact" in footer.text
