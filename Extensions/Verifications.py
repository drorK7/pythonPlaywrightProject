# extensions/Verifications.py

from PageObjects.Locators.MainPage import MainPage
from playwright.sync_api import Page


class Verifications:
    def __init__(self, page: Page):
        self.page = page

    def validate_members_per_page(self):
        main_page = MainPage(self.page)
        member_item = "tr[class='MuiTableRow-root css-1gqug66']"
        # Wait for the member items to load
        self.page.wait_for_selector(member_item, timeout=5000)
        member_elements = self.page.query_selector_all(member_item)
        num_of_members = len(member_elements)
        assert num_of_members == 10, f"Expected 10 members per page, but found {num_of_members}."
