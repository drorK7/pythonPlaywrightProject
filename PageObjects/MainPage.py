from playwright.sync_api import Page, Locator


class MainPage:
    def __init__(self, page):
        self.page = page

    @property
    def next_page_button(self) -> Locator:
        return self.page.locator("svg[data-testid='ArrowRightIcon']")

    @property
    def back_page_button(self) -> Locator:
        return self.page.locator("svg[data-testid='ArrowLeftIcon']")

    @property
    def page_number_input(self) -> Locator:
        return self.page.locator("input[class='MuiInputBase-input MuiInput-input css-mnn31'][value]")

    @property
    def members_items(self) -> Locator:
        return self.page.locator("tr[class='MuiTableRow-root css-1gqug66']")

    @property
    def results_count(self) -> Locator:
        return self.page.locator('//*[contains(@id, "result-stats")]')

    @property
    def search_time(self) -> Locator:
        return self.page.locator('//*[contains(@id, "result-stats")]/nobr')


