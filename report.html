import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_spotify_search_functional(driver):
    wait = WebDriverWait(driver, 20)

    driver.get("https://open.spotify.com/search")

    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='search-input']")))
    search_input.click()
    search_input.send_keys("Imagine Dragons")

    time.sleep(5)

    assert "Imagine Dragons" in driver.page_source


def test_spotify_main_page_load(driver):
    driver.get("https://open.spotify.com/")
    wait = WebDriverWait(driver, 20)

    time.sleep(3)
    assert "Spotify" in driver.title
