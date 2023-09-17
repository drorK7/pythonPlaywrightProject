# tests/test_add_new_member.py

import pytest
from playwright.sync_api import sync_playwright
from Utilities.CommonOps import browser
from Configuration.Configuration import URL


def test_add_new_member(browser):
    page = browser.new_page()
    page.goto(URL)

    add_member_button_selector = "svg[data-testid='PersonAddIcon']"
    name_input_selector = "(//input['MuiOutlinedInput-notchedOutline css-igs3ac'])[2]"
    family_input_selector = "(//input['MuiOutlinedInput-notchedOutline css-igs3ac'])[3]"
    add_button_selector = "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium"

    # Click the "Add Member" button to open the add member form
    page.click(add_member_button_selector)

    # Fill in the member details (firstName and familyName)
    page.fill(name_input_selector, "New Member First Name")
    page.fill(family_input_selector, "New Member Family Name")

    # Click the "Add" button to add the new member
    page.click(add_button_selector)

    row_locator = "tr[class='MuiTableRow-root css-1gqug66']"

    # Wait for the table rows to load (you can adjust the timeout as needed)
    page.wait_for_selector(row_locator, timeout=10000)

    # Find the newly added member in the table and validate the text
    added_first_name = "New Member First Name"
    added_family_name = "New Member Family Name"

    rows = page.query_selector_all(row_locator)
    found = False

    for row in rows:
        firstName_locator = "//td['MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-q34dxg']"
        familyName_locator = "//td['MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-q34dxg']"

        firstName = row.query_selector(firstName_locator).inner_text()
        familyName = row.query_selector(familyName_locator).inner_text()

        if firstName == added_first_name and familyName == added_family_name:
            found = True
            break

    assert found, f"Newly added member ({added_first_name}, {added_family_name}) not found in the table."

    page.close()
