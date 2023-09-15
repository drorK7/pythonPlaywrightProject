from playwright.sync_api import Page, BrowserContext

import PageObjects
from .ProjectBase import Base  # Import your Base class from the Utilities package

class ManagePages(Base):
    @staticmethod
    def init():
        Base.googleLogin = PageObjects.mainPage(Base.driver)
        Base.zapMainPage = PageObjects.ZapMainPage(Base.driver)
