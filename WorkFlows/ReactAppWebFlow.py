import pytest
from playwright.sync_api import Page, Keyboard
from Extensions.UiActions import UiActions
import pytest
from playwright.sync_api import Page, Keyboard
from Extensions.UiActions import UiActions
from Extensions.Verifications import Verifications
from Utilities.CommonOperations import CommonOperations


class TestReactAppWebFlows(CommonOperations):

    @pytest.mark.parametrize("pageTitle", ["Page Title 1", "Page Title 2"])
    def test_application_loads_successfully(self, pageTitle):
        page = self.page
        ui_actions = UiActions(page)
        assert ui_actions.get_page_title() == pageTitle, "Application failed to load"

