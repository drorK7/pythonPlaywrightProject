# tests/test_default_member_list.py

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_default_member_list(browser):
    page = browser.new_page()
    page.goto("http://192.168.1.49:3000/")

    member_list_selector = "div[class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiTableContainer-root css-13xy2my']"

    # Wait for the member list to load (you can adjust the timeout as needed)
    page.wait_for_selector(member_list_selector, timeout=5000)

    # Check if the member list is displayed on the first page
    is_member_list_displayed = page.is_visible(member_list_selector)

    assert is_member_list_displayed, "Default member list is not displayed on the first page."

    page.close()
