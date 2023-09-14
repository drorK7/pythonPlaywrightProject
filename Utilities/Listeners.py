import os

import pytest
import base
import CommonOperations
from pytest import fixture
from pytest import request
from playwright.sync_api import Page, BrowserContext
from io import BytesIO
from xml.etree import ElementTree as et


class Listeners(CommonOperations):
    @staticmethod
    def on_finish(test):
        print("------------------- Test " + test.name + " Completed! -------------------")

    @staticmethod
    def on_start(test):
        print("------------------- Test " + test.name + " is Starting! -------------------")

    @staticmethod
    def on_test_failure(test):
        print("------------------- The test " + test.name + " has failed! -------------------")
        if not CommonOperations.get_data("PlatformName").lower() == "api":
            Listeners.save_screenshot()

    @staticmethod
    def on_test_skipped(test):
        print("------------------- Test " + test.name + " is Skipping! -------------------")

    @staticmethod
    def on_test_start(test):
        print("------------------- Test " + test.name + " successfully started! -------------------")

    @staticmethod
    def on_test_success(test):
        print("------------------- Test successfully completed! -------------------")

    @staticmethod
    def save_screenshot(test):
        screenshot = test.driver.screenshot()
        screenshot_path = os.path.join("screenshots", f"{test.name}.png")
        screenshot.save_as(screenshot_path)

    @fixture(scope="function", autouse=True)
    def test_listener(self, request):
        request.node._testcase.instance = self
        request.addfinalizer(self.on_finish(request.node))
        return self

    @staticmethod
    def get_data(node_name):
        config_file = os.path.join(".", "Configuration", "Configuration.xml")
        try:
            tree = et.parse(config_file)
            root = tree.getroot()
            return root.find(node_name).text
        except Exception as e:
            print("Exception in reading XML file:", e)
