# tests/test_application_load.py

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_application_loads_successfully(browser):
    page = browser.new_page()
    page.goto("http://192.168.1.49:3000/")
    assert page.title() == "React App"
    page.close()
