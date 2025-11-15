from behave import then

@then('The page title should contain "{text}"')
def step_title_contains(context, text):
    assert text.lower() in context.driver.title.lower()
