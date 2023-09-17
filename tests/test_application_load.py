# tests/test_application_load.py
import pytest
from playwright.sync_api import sync_playwright
from Utilities.CommonOperations import CommonOperations
from Configuration.config import URL
from Extensions.UiActions import UiActions
from Utilities.CommonOps import browser


@pytest.mark.parametrize("page_title", ["React App"])
def test_application_loads_successfully(page_title, browser):
    page = browser.new_page()
    page.goto(URL)
    ui_actions = UiActions(page)
    assert ui_actions.get_page_title() == page_title, "Application failed to load"
    page.close()
