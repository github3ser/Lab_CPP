from behave import given, when, then
from pages.google_page import GooglePage

@given("I open the Google homepage")
def step_open_homepage(context):
    context.page = GooglePage(context.driver)
    context.page.open_home()

@then("I should see the Google search box")
def step_see_search_box(context):
    assert context.page.find(("name", "q"))

@when('I search for "{text}"')
def step_search(context, text):
    context.page.type_search(text)
    context.page.search_enter()

@then("I should see multiple search results")
def step_results(context):
    assert len(context.page.get_results()) > 0

@when("I press search button without input")
def step_search_without_input(context):
    context.page.click_search_button()

@then("The page should remain on Google homepage")
def step_stay_on_home(context):
    assert "google" in context.driver.current_url.lower()

@then("I should see a Did You Mean suggestion")
def step_did_you_mean(context):
    assert context.page.has_did_you_mean()
