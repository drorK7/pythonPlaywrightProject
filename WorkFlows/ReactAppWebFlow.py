import pytest
from playwright.sync_api import Page, Keyboard
from Extensions.UiActions import UiActions
from Extensions.Verifications import Verifications
from Utilities.CommonOperations import CommonOperations


class ReactAppWebFlows(CommonOperations):

    @pytest.mark.parametrize("pageTitle", "Page Title 1")
    def test_application_loads_successfully(self, pageTitle):
        page = self.page
        ui_actions = UiActions(page)
        assert ui_actions.get_page_title() == pageTitle, "Application failed to load"

    #
    # @pytest.mark.parametrize("text2Search", ["Michael Jordan"])
    # def test_verify_page_header(self, text2Search):
    #     page = self.page
    #     ui_actions = UiActions(page)
    #
    #     ui_actions.click(googleLogin.search_txt_box)
    #     ui_actions.fill_input_field(googleLogin.search_txt_box, text2Search)
    #     ui_actions.send_keyboard_key(googleLogin.search_txt_box, Keyboard.Key.RETURN)
    #     ui_actions.wait_until_appears(googleLogin.search_form, 10)
    #
    #     assert ui_actions.get_page_title() == "Michael Jordan - חיפוש ב-Google"
    #
    # @pytest.mark.parametrize("text2Search", ["Michael Jordan"])
    # def test_print_search_results_counter_and_time(self, text2Search):
    #     page = self.page
    #     ui_actions = UiActions(page)
    #
    #     ui_actions.click(googleLogin.search_txt_box)
    #     ui_actions.fill_input_field(googleLogin.search_txt_box, text2Search)
    #     ui_actions.send_keyboard_key(googleLogin.search_txt_box, Keyboard.Key.RETURN)
    #     ui_actions.wait_until_appears(googleLogin.search_form, 10)
    #
    #     results_count = ui_actions.get_element_value(googleLogin.results_count)
    #     search_time = ui_actions.get_element_value(googleLogin.search_time)
    #
    #     print("******** The search results count is:", results_count, "********\n",
    #           "******** The search time is:", search_time, "seconds ********")
    #
    # @pytest.mark.parametrize("text2Search", ["Michael Jordan"])
    # def test_validate_web_logo(self, text2Search):
    #     page = self.page
    #     ui_actions = UiActions(page)
    #     verifications = Verifications(page)
    #
    #     ui_actions.click(googleLogin.search_txt_box)
    #     ui_actions.fill_input_field(googleLogin.search_txt_box, text2Search)
    #     ui_actions.send_keyboard_key(googleLogin.search_txt_box, Keyboard.Key.RETURN)
    #     ui_actions.wait_until_appears(googleLogin.search_form, 10)
    #
    #     verifications.visual_element(googleLogin.icon_google, "Google Home")
