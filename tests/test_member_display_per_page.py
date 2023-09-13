# tests/test_member_display_per_page.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_members_display_per_page(browser):
    page = browser.new_page()
    page.goto("http://192.168.1.49:3000/")

    member_item_selector = "tr[class='MuiTableRow-root css-1gqug66']"

    # Wait for the member items to load
    page.wait_for_selector(member_item_selector, timeout=5000)

    # Count the number of displayed member items on the page
    member_items = page.query_selector_all(member_item_selector)
    num_member_items = len(member_items)

    assert num_member_items == 10, f"Expected 10 members per page, but found {num_member_items}."

    page.close()
