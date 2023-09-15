import os
import pytest
from playwright.sync_api import Page, Locator
from Utilities import CommonOperations

class Verifications:
    def __init__(self, page: Page):
        self.page = page
        self.common_operations = CommonOperations()  # Create an instance of CommonOperations

    def validate_text_in_element(self, element: Locator, expected_value: str):
        actual_text = element.inner_text()
        assert actual_text == expected_value, f"Expected text: '{expected_value}', Actual text: '{actual_text}'"
