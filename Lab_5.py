from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Setări Chrome for Testing ===
chromedriver_path = r"D:\Documents\Anul_4_sem.7\Lab CPP\Lab 5\chromedriver-win64\chromedriver.exe"
chrome_for_testing_path = r"D:\Documents\Anul_4_sem.7\Lab CPP\Lab 5\chrome-win64\chrome.exe"

options = Options()
options.binary_location = chrome_for_testing_path

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Deschide 999.md
    driver.get("https://999.md")

    # Așteaptă până când bara de search e vizibilă
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )
    print("999.md search box (header) is visible.")

    # Introduce termenul "computer"
    search_box.clear()
    search_box.send_keys("computer")

    # Apasă butonul de search
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="search-button"]')
    search_button.click()

    # Așteaptă cel puțin un anunț să fie încărcat după căutare
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="photo-item-title"]'))
    )
    print("Search results loaded successfully.")
    print("Current URL:", driver.current_url)

except Exception as e:
    print("Test failed:", e)

finally:
    time.sleep(2)
    driver.quit()
