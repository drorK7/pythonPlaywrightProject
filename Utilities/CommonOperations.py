import pytest
import os
from Utilities.ProjectBase import ProjectBase
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, BrowserContext
from requests import Session
from xml.etree import ElementTree as et


class CommonOperations(ProjectBase):
    # Read XML Function
    @staticmethod
    def get_data(node_name):
        config_file = os.path.join(".", "Configuration", "Configuration.xml")
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
            ProjectBase.driver = CommonOperations.init_chrome_driver()
        elif browser_type.lower() == "firefox":
            ProjectBase.driver = CommonOperations.init_ff_driver()
        elif browser_type.lower() == "edge":
            ProjectBase.driver = CommonOperations.init_edge_driver()
        else:
            raise RuntimeError("Invalid browser name")

        ProjectBase.driver.context().new_page()
        ProjectBase.driver.context().clear_cookies()
        ProjectBase.driver.goto(CommonOperations.get_data("url"))

    # Initializing Google Chrome browser
    @staticmethod
    def init_chrome_driver():
        CommonOperations.initialize_playwright()
        return ProjectBase.driver

    # Initializing FireFox browser
    @staticmethod
    def init_ff_driver():
        CommonOperations.initialize_playwright()
        return ProjectBase.driver

    # Initializing Edge browser
    @staticmethod
    def init_edge_driver():
        CommonOperations.initialize_playwright()
        return ProjectBase.driver

    # Get the selected testing platform and initializing the corresponding function
    @pytest.fixture(scope="class", autouse=True)
    def start_session(self):
        if CommonOperations.get_data("PlatformName").lower() == "web":
            CommonOperations.init_browser(CommonOperations.get_data("BrowserName").lower())
        elif CommonOperations.get_data("PlatformName").lower() == "api":
            CommonOperations.init_api()
        else:
            raise RuntimeError("Invalid platform name")
        # ManagePages.init()  # You can replace this with the appropriate Python class for page management

    @pytest.fixture(autouse=True)
    def after_method(self):
        if CommonOperations.get_data("PlatformName").lower() == "web":
            ProjectBase.driver.reload()

    # Closing the session
    @pytest.fixture(scope="class", autouse=True)
    def close_session(self):
        if CommonOperations.get_data("PlatformName").lower() != "api":
            CommonOperations.close_playwright()
