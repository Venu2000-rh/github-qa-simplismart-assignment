from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


##### Sign-Up is skipped since I had already signed up during manual validation ####

def test_login_valid_user(browser):
    assert "Home" in browser.page_source


def test_login_with_empty_credentials():
    from selenium import webdriver
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get("https://github.com/login")

    sign_in_btn = wait.until(EC.element_to_be_clickable((By.NAME, "commit")))
    sign_in_btn.click()

    assert browser.current_url == "https://github.com/login", "Expected to remain on login page for empty credentials"

    browser.quit()


def test_login_with_invalid_credentials():
    from selenium import webdriver
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get("https://github.com/login")

    browser.find_element(By.ID, "login_field").send_keys("invalid_user@example.com")
    browser.find_element(By.ID, "password").send_keys("wrongpassword123")

    browser.find_element(By.NAME, "commit").click()

    wait.until(EC.url_contains("/session"))
    assert "/session" in browser.current_url, "Expected redirect to /session for invalid credentials"

    browser.quit()
