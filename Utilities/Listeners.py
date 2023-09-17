import os
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from io import BytesIO
from xml.etree import ElementTree as et


class Listeners:
    def __init__(self):
        self.screenshot_dir = os.path.join(os.getcwd(), "screenshots")

    @pytest.fixture(scope="module", params=["chromium", "firefox", "webkit"])
    def browser(self, request):
        with sync_playwright() as p:
            browser_type = request.param
            browser = getattr(p, browser_type).launch(headless=False)
            yield browser
            browser.close()

    @pytest.fixture(scope="function")
    def page(self, browser):
        page = browser.new_page()
        yield page
        page.close()

    @pytest.fixture(scope="function", autouse=True)
    def screenshot_on_failure(self, request, page):
        def on_failure():
            screenshot = page.screenshot()
            screenshot_path = os.path.join(self.screenshot_dir, f"{request.node.name}.png")
            screenshot.save_as(screenshot_path)

        request.addfinalizer(on_failure)

    @pytest.fixture(scope="function", autouse=True)
    def test_listener(self, request):
        print("------------------- Test " + request.node.name + " is Starting! -------------------")

        def on_finish():
            print("------------------- Test " + request.node.name + " Completed! -------------------")

        request.addfinalizer(on_finish)

        request.node._testcase.instance = self  # Attach the Listeners instance to the instance
        return self

    def get_data(self, node_name):
        config_file = os.path.join(".", "Configuration", "Configuration.xml")
        try:
            tree = et.parse(config_file)
            root = tree.getroot()
            return root.find(node_name).text
        except Exception as e:
            print("Exception in reading config file:", e)

    # Define an on_finish method for cleanup
    def on_finish(self):
        print("------------------- Tests Completed! Cleaning up... -------------------")
        # Perform any cleanup tasks here, if needed

