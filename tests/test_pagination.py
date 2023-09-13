# tests/test_pagination.py

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_pagination(browser):
    page = browser.new_page()
    page.goto("http://192.168.1.49:3000/")

    next_page_button_selector = "svg[data-testid='ArrowRightIcon']"
    page_number_selector = "(//input['MuiOutlinedInput-notchedOutline css-igs3ac'])[1]"

    # Wait for the pagination elements to load
    page.wait_for_selector(next_page_button_selector, timeout=5000)

    # Check if all 10 pages can be navigated
    for page_number in range(1, 10):
        # Click the next page button
        page.click(next_page_button_selector)

        # Wait for the page number to update
        page.wait_for_selector(page_number_selector, timeout=5000)

        # Check if the current page number matches the expected page number
        current_page_number = int(page.text_content(page_number_selector))
        assert current_page_number == page_number, "Failed to navigate to page {page_number}"

    page.close()
