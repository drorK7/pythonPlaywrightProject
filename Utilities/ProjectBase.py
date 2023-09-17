from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, BrowserContext
from PageObjects import MainPage


class ProjectBase:
    driver: Page = None
    wait = None
    action = None
    imageScreenshot = None
    imgDif = None
    dif = None
    ImageChops = None

    Platform = None
    mainPage = None

    httpRequest = None
    response = None
    requestParams = {}
    jp = None

    @staticmethod
    def initialize_playwright():
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            ProjectBase.driver = context.new_page()

    @staticmethod
    def close_playwright():
        if ProjectBase.driver:
            ProjectBase.driver.context().close()
            ProjectBase.driver = None
