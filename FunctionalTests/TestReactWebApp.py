import pytest
from Utilities.CommonOperations import CommonOperations
from WorkFlows.ReactAppWebFlow import ReactAppWebFlows
from playwright.sync_api import sync_playwright, Page


class TestReactWebApp(CommonOperations):
    def __init__(self, page: Page):
        self.page = page
        self.common_operations = CommonOperations()  # Create an instance of CommonOperations

    @pytest.mark.parametrize("search_phrase", ["Search Phrase 1", "Search Phrase 2"])
    def test_application_loaded_successfully(self, search_phrase):
        ReactAppWebFlows.test_application_loads_successfully(self.common_operations.get_data(search_phrase))
