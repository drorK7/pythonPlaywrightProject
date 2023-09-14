from playwright.sync_api import Page, Locator


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def search_txt_box(self) -> Locator:
        return self.page.locator('input[name="q"]')

    @property
    def search_form(self) -> Locator:
        return self.page.locator('#searchform')

    @property
    def search_results(self) -> Locator:
        return self.page.locator('//*[contains(@class, "TzHB6b cLjAic K7khPe")]')

    @property
    def results_count(self) -> Locator:
        return self.page.locator('//*[contains(@id, "result-stats")]')

    @property
    def search_time(self) -> Locator:
        return self.page.locator('//*[contains(@id, "result-stats")]/nobr')

    @property
    def search_query_field(self) -> Locator:
        return self.page.locator('input[name="q"]')

    @property
    def icon_google(self) -> Locator:
        return self.page.locator('img[src="/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"]')
