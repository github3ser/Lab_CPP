from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.header_page import HeaderPage

@given("utilizatorul este pe pagina de start")
def step_go_home(context):
    context.driver.get("https://adoring-pasteur-3ae17d.netlify.app/mens.html")


@when("click pe primul item din meniu")
def step_click_first(context):
    first = context.driver.find_elements(*HeaderPage.MENU_ITEMS)[0]
    first.click()


@when("click pe al doilea item din meniu")
def step_click_second(context):
    second = context.driver.find_elements(*HeaderPage.MENU_ITEMS)[1]
    second.click()


@then("pagina se încarcă fără eroare")
def step_no_404(context):
    assert "404" not in context.driver.page_source, "Pagina a dat eroare 404"


@when("click pe fiecare link din meniu și apoi Back")
def step_click_all(context):
    menu_length = len(context.driver.find_elements(*HeaderPage.MENU_ITEMS))

    for i in range(menu_length):
        # refacem lista de linkuri
        links = context.driver.find_elements(*HeaderPage.MENU_ITEMS)
        links[i].click()

        # verificăm că nu apare eroare 404
        assert "404" not in context.driver.page_source, f"Eroare 404 după click pe linkul {i}"

        # revenim explicit pe pagina principală
        context.driver.get("https://adoring-pasteur-3ae17d.netlify.app/")


@then("utilizatorul revine pe homepage")
def step_back(context):
    assert context.driver.current_url.lower() == "https://adoring-pasteur-3ae17d.netlify.app/", \
        f"Nu s-a revenit pe homepage, URL curent: {context.driver.current_url}"


@when("utilizatorul face click pe meniuri cu submeniuri")
def step_click_dropdowns(context):
    # Men's wear
    men_dropdown = context.driver.find_element(*HeaderPage.MEN_DROPDOWN)
    men_dropdown.click()
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(HeaderPage.MEN_CLOTHING)
    )
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(HeaderPage.MEN_ACCESSORIES)
    )

    # Women's wear
    women_dropdown = context.driver.find_element(*HeaderPage.WOMEN_DROPDOWN)
    women_dropdown.click()
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(HeaderPage.WOMEN_CLOTHING)
    )
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(HeaderPage.WOMEN_ACCESSORIES)
    )

@then("submeniurile sunt vizibile și funcționează")
def step_submenus_click(context):
    # Men's wear dropdown
    men_dropdown = context.driver.find_element(*HeaderPage.MEN_DROPDOWN)
    men_dropdown.click()  # deschide dropdown-ul

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.MEN_CLOTHING)
    ).click()  # click pe Clothing

    context.driver.back()  # revenire

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.MEN_DROPDOWN)
    ).click()  # redeschide dropdown

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.MEN_ACCESSORIES)
    ).click()  # click pe Accessories

    context.driver.back()

    # Women's wear dropdown
    women_dropdown = context.driver.find_element(*HeaderPage.WOMEN_DROPDOWN)
    women_dropdown.click()  # deschide dropdown

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.WOMEN_CLOTHING)
    ).click()

    context.driver.back()

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.WOMEN_DROPDOWN)
    ).click()  # redeschide

    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(HeaderPage.WOMEN_ACCESSORIES)
    ).click()

    context.driver.back()
