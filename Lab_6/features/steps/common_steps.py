from behave import given

@given('utilizatorul deschide pagina "{url}"')
def step_open_page(context, url):
    context.driver.get(url)