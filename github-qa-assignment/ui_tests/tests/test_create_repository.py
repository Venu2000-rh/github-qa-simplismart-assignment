from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_create_repository(browser):
    browser.get("https://github.com/new")
    wait = WebDriverWait(browser, 20)

    repo_name = f"qa-selenium-{int(time.time())}"

    # Fill repo name
    repo_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-describedby*="RepoNameInput"]'))
    )
    repo_input.send_keys(repo_name)

    time.sleep(2)  # Let GitHub validate repo name

    # ✅ Locate the real button via its span label
    create_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Create repository']/ancestor::button"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", create_btn)
    create_btn.click()

    # ✅ Confirm success
    assert "Quick setup" in browser.page_source or "Code" in browser.page_source

    print(f"✅ Repository created: {repo_name}")
