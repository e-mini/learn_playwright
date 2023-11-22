from playwright.sync_api import expect
from pages.home_page import HomePage

import pytest


class TestAuthentication:
    def test_can_register(self, page, create_user):
        home_page = HomePage(page)
        expect(home_page.account_created_message).to_be_visible()
        expect(home_page.log_out_link).to_be_visible()


    def test_can_still_login(self, page, create_user):
        created_user_object = create_user
        home_page = HomePage(page)
        home_page.load(page)
        home_page.test_login(created_user_object["user_name"], created_user_object["password"])
        expect(home_page.log_out_link).to_be_visible()

        home_page.log_out_link.click()


