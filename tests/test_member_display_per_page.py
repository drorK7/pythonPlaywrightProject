# tests/test_member_display_per_page.py

import pytest
from Configuration.config import URL
from PageObjects.MainPage import MainPage
from Utilities.CommonOps import browser, page  # Import fixtures from CommonOps module


@pytest.fixture
def setup(browser, page):
    main_page = MainPage(page)
    page.goto(URL)
    yield main_page
    page.close()


def test_members_display_per_page(setup, page):
    main_page = setup
    # Wait for the member items to load
    page.wait_for_selector(main_page.members_items, timeout=5000)

    # Count the number of displayed member items on the page
    member_elements = page.query_selector_all(main_page.members_items)
    num_of_members = len(member_elements)
    assert num_of_members == 10, f"Expected 10 members per page, but found {num_of_members}."
