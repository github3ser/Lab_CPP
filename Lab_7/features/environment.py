from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def before_all(context):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

        driver_path = os.path.join(project_root, "chromedriver-win64", "chromedriver.exe")
        chrome_path = os.path.join(project_root, "chrome-win64", "chrome.exe")

        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        context.driver = webdriver.Chrome(
            service=Service(driver_path),
            options=options
        )

        context.driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                """
            }
        )

def after_scenario(context, scenario):
    screenshot_name = scenario.name.replace(" ", "_") + ".png"
    screenshot_path = os.path.join("screenshots", screenshot_name)

    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#rcnt"))
        )
    except:
        pass

    context.driver.save_screenshot(screenshot_path)

def after_all(context):
    context.driver.quit()
