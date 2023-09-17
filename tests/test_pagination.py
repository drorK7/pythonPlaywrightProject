# tests/test_pagination.py

import pytest
from playwright.sync_api import sync_playwright
from Configuration.Configuration import URL
from Utilities.CommonOps import browser
from Extensions.Verifications import Verifications
from PageObjects.MainPage import MainPage
from Utilities.CommonOps import browser, page  # Import fixtures from CommonOps module
from Utilities.Listeners import Listeners

# Define a global variable to store the Listeners instance
listeners = None
last_page = "9"

@pytest.fixture(autouse=True)
def test_listener(request):
    global listeners
    listeners = Listeners()
    yield listeners
    listeners.on_finish()


@pytest.fixture
def setup(browser, page):
    main_page = MainPage(page)
    page.goto(URL)
    yield main_page
    page.close()


@pytest.mark.sanity
def test_fw_pagination_using_right_arrow_button(setup, page):
    main_page = setup
    next_button = main_page.next_page_button
    # Wait for the pagination elements to load
    page.wait_for_selector(next_button, timeout=5000)
    verifications = Verifications(page)
    for page_number in range(1, 10):
        # Click the next page button
        page.click(next_button)
        verifications.validate_members_per_page()


def test_backward_pagination_using_left_arrow_button(setup, page):
    main_page = setup
    backward_button = "svg[data-testid='ArrowLeftIcon']"
    input_page_number = "input[class='MuiInputBase-input MuiInput-input css-mnn31'][value]"
    verifications = Verifications(page)
    # Skip to the last page:
    page.keyboard.press("Control+Shift+ArrowLeft")
    page.keyboard.press("Backspace")
    page.fill(input_page_number, last_page)
    page.keyboard.press("Enter")
    page.wait_for_selector(backward_button, timeout=5000)
    for page_number in range(9, 1):
        page.click(backward_button)
        verifications.validate_members_per_page()


def test_pagination_using_input(setup):
    page = setup
    next_button = "svg[data-testid='ArrowRightIcon']"
    input_page_number = "input[class='MuiInputBase-input MuiInput-input css-mnn31'][value]"
    verifications = Verifications(page)
    for page_number in range(1, 10):
        page.click(input_page_number)
        # Clear any existing text in the input field
        page.keyboard.press("Control+Shift+ArrowLeft")
        page.keyboard.press("Backspace")
        page.fill(input_page_number, str(page_number))
        page.keyboard.press("Enter")
        page.wait_for_selector(next_button, timeout=5000)
        verifications.validate_members_per_page()
