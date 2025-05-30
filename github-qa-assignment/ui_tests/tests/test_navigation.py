import time
from selenium.webdriver.common.by import By


def test_navigate_repo_tabs(browser):
    base_url = "https://github.com/venugopal-2000/qa-selenium-1748622025"

    tabs = ["", "/issues", "/pulls", "/actions"]
    for tab in tabs:
        browser.get(base_url + tab)
        time.sleep(1)
        assert "GitHub" in browser.title


def test_ui_consistency(browser):
    browser.get("https://github.com/venugopal.fitbiz@gmail.com/flexiple-simplismart-qa-assignment")
    navbar = browser.find_element(By.CLASS_NAME, "UnderlineNav")
    assert navbar is not None
