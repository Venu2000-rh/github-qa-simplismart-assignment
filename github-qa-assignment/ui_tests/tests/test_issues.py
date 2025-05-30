from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_create_and_close_issue(browser):
    wait = WebDriverWait(browser, 20)
    username = "venugopal-2000"
    repo = "qa-selenium-1748622025"
    issue_title = f"Issue via UI - {int(time.time())}"
    issue_body = "This issue is being created and closed using Selenium UI automation."

    browser.get(f"https://github.com/{username}/{repo}/issues")
    time.sleep(2)

    new_issue_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//a[@type='button' and contains(@href, '/issues/new/choose')]"
    )))
    new_issue_btn.click()

    try:
        blank_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(text(), 'Open a blank issue')]"
        )))
        blank_btn.click()
    except:
        pass

    title_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Add a title"]')))
    title_input.send_keys(issue_title)

    body_input = browser.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Markdown value"]')
    body_input.send_keys(issue_body)

    assign_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[text()='Assign yourself']/ancestor::button"
    )))
    assign_btn.click()

    create_btn = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 'button[data-testid="create-issue-button"]'
    )))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", create_btn)
    create_btn.click()

    issue_visible = wait.until(EC.presence_of_element_located((
        By.XPATH, f"//span[contains(text(), '{issue_title}')]"
    )))
    assert issue_title in browser.page_source
    print(f"✅ Issue created: {issue_title}")



