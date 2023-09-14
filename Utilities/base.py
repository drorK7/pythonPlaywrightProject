from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, BrowserContext
from PageObjects import MainPage


class base:
    driver: Page = None
    wait = None
    action = None
    imageScreenshot = None
    imgDif = None
    dif = None
    ImageChops = None

    Platform = None
    mainPage = None  # You can replace this with the appropriate Python class for Google login

    httpRequest = None
    response = None
    requestParams = {}
    jp = None

    @staticmethod
    def initialize_playwright():
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            base.driver = context.new_page()

    @staticmethod
    def close_playwright():
        if base.driver:
            base.driver.context().close()
            base.driver = None
