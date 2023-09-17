from playwright.sync_api import Page, BrowserContext

import PageObjects
from .ProjectBase import ProjectBase  # Import your Base class from the Utilities package


class ManagePages(ProjectBase):
    @staticmethod
    def init():
        ProjectBase.mainPage = PageObjects.mainPage(ProjectBase.driver)
