import pytest
import os
from Utilities.ProjectBase import ProjectBase
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, BrowserContext
from requests import Session
from xml.etree import ElementTree as et


class CommonOperations(ProjectBase):
    def __init__(self):
        super().__init__()

    # Read XML Function
    @staticmethod
    def get_data(node_name):
        path = r'C:\Users\Doron\PycharmProjects\pythonPlaywrightProject\Configuration\Configuration.xml'
        config_file = os.path.join(path, "Configuration", "Configuration.xml")
        try:
            tree = et.parse(config_file)
            root = tree.getroot()
            return root.find(node_name).text
        except Exception as e:
            print("Exception in reading XML file:", e)

    # Initializing web platform with browser selection: Google Chrome/FireFox/Microsoft Edge
    @staticmethod
    def init_browser(browser_type):
        if browser_type.lower() == "chrome":
            CommonOperations.driver = CommonOperations.init_chrome_driver()
        elif browser_type.lower() == "firefox":
            CommonOperations.driver = CommonOperations.init_ff_driver()
        elif browser_type.lower() == "edge":
            CommonOperations.driver = CommonOperations.init_edge_driver()
        else:
            raise RuntimeError("Invalid browser name")

        CommonOperations.driver.context().new_page()
        CommonOperations.driver.context().clear_cookies()
        CommonOperations.driver.goto(CommonOperations.get_data("url"))

    @pytest.fixture(scope="class", autouse=True)
    def start_session(self):
        platform_name = CommonOperations.get_data("PlatformName")
        if platform_name is not None and platform_name.lower() == "web":
            CommonOperations.init_browser(CommonOperations.get_data("BrowserName").lower())
        elif platform_name is not None and platform_name.lower() == "api":
            CommonOperations.init_api()
        else:
            raise RuntimeError("Invalid platform name")

    @pytest.fixture(autouse=True)
    def after_method(self):
        if CommonOperations.get_data("PlatformName").lower() == "web":
            CommonOperations.driver.reload()

    @pytest.fixture(scope="class", autouse=True)
    def close_session(self):
        if CommonOperations.get_data("PlatformName").lower() != "api":
            CommonOperations.close_playwright()

    @classmethod
    def init_chrome_driver(cls):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            yield browser
            browser.close()
        pass

    @classmethod
    def init_ff_driver(cls):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            yield browser
            browser.close()
        pass

    @classmethod
    def init_edge_driver(cls):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="msedge", headless=False)
            yield browser
            browser.close()
        pass
