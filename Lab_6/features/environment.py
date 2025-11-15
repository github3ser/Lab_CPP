from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def before_all(context):
    print("=== before_all is running ===")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    driver_path = os.path.join(project_root, "chromedriver-win64", "chromedriver.exe")
    chrome_path = os.path.join(project_root, "chrome-win64", "chrome.exe")

    if not os.path.exists(chrome_path):
        print(f"Chrome for Testing nu a fost găsit: {chrome_path}")
        raise SystemExit()

    options = Options()
    options.binary_location = chrome_path
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(5)

def after_all(context):
    print("=== after_all is running ===")
    if hasattr(context, "driver"):
        context.driver.quit()
