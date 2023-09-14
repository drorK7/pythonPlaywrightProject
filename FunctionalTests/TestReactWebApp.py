import pytest
from Utilities.CommonOperations import CommonOperations
from WorkFlows.ReactAppWebFlow import ReactAppWebFlows
from playwright.sync_api import sync_playwright, Page


class TestReactWebApp(CommonOperations):
    def __init__(self, page: Page):
        self.page = page
        self.common_operations = CommonOperations()  # Create an instance of CommonOperations

    @pytest.mark.parametrize("search_phrase")
    def test_application_loaded_successfully(self, search_phrase):
        ReactAppWebFlows.test_application_loads_successfully(self.common_operations.get_data(search_phrase))

    # @pytest.mark.parametrize("search_phrase", ["Michael Jordan"])
    # def test_verify_page_title(self, search_phrase):
    #     GoogleFlows.verify_page_header(search_phrase)
    #
    # @pytest.mark.parametrize("search_phrase", ["Michael Jordan"])
    # def test_display_search_count_and_time(self, search_phrase):
    #     GoogleFlows.print_search_results_counter_and_time(search_phrase)
    #
    # @pytest.mark.parametrize("search_phrase", ["Michael Jordan"])
    # def test_validate_logo(self, search_phrase):
    #     GoogleFlows.validate_web_logo(search_phrase)
