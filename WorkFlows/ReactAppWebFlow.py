import pytest
from playwright.sync_api import Page, sync_playwright
from Extensions.UiActions import UiActions
from Utilities.CommonOperations import CommonOperations


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


class TestReactAppWebFlows(CommonOperations):

    @pytest.mark.parametrize("page_title", ["React App", "Page Title 2"])
    def test_application_loads_successfully(self, page_title, browser):
        page = browser.new_page()
        page.goto('http://192.168.1.49:3000/')
        ui_actions = UiActions(page)
        assert ui_actions.get_page_title() == page_title, "Application failed to load"
