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

    def visual_element(self, image_element: Locator, expected_image_path: str):
        # Capture a screenshot of the current element
        screenshot = image_element.screenshot()

        # Save the screenshot to a file
        screenshot_path = os.path.join(self.common_operations.get_data("ScreenshotDir"), "actual_image.png")
        with open(screenshot_path, "wb") as file:
            file.write(screenshot)

        # Optionally, you can save the expected image file path in your configuration
        expected_image_path = os.path.join(self.common_operations.get_data("ImageRepo"), expected_image_path + ".png")

        # Compare the actual screenshot with the expected image using your preferred image comparison library or method

# def test_image_comparison(step_description, image_element, expected_image_path):
#     # Create an instance of the Verifications class
#     verifications = Verifications(page_instance)
#
#     # Use the Verifications class methods with step descriptions
#     verifications.visual_element(image_element, expected_image_path)
