from playwright.sync_api import Page, ElementHandle, Keyboard
from playwright.sync_api import Locator, Response

class UiActions:
    def __init__(self, page: Page):
        self.page = page

    def click(self, element: Locator):
        element.click()

    def fill_input_field(self, element: Locator, text: str):
        element.fill(text)

    def send_keyboard_key(self, element: Locator, key: Keyboard):
        element.press(key)

    def get_page_title(self) -> str:
        return self.page.title()

    def get_element_value(self, element: Locator) -> str:
        return element.text()

    def hover(self, element: Locator):
        element.hover()

    def wait_until_appears(self, element: Locator, seconds_to_wait: int):
        element.wait_for_timeout(seconds_to_wait * 1000)

    def check_exists(self, element: ElementHandle, text: str) -> bool:
        if not element or not text:
            return False
        return text in element.text()

    def check_exists_in_elements(self, elements: [ElementHandle], text: str) -> bool:
        if not elements or not text:
            return False
        for element in elements:
            if text in element.text():
                return True
        return False
