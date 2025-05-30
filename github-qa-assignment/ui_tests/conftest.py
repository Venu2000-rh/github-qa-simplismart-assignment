import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://github.com/login")
    driver.find_element(By.ID, "login_field").send_keys("venugopal.fitbiz@gmail.com")
    driver.find_element(By.ID, "password").send_keys("hublidharwad@2000")
    driver.find_element(By.NAME, "commit").click()
    yield driver
    driver.quit()

