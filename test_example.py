import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_can_login(page: Page):
    # setup
    page.goto("https://the-internet.herokuapp.com/login")

    # test
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator(".radius").click()

    # assertion
    expect(page.locator("#flash-messages")).to_be_visible()
    expect(page.locator(".secondary")).to_be_visible()

    # tear down
    page.locator(".secondary").click()


    # homework
    # registration test
def test_can_register(page: Page):
    home_page = HomePage(page)
    home_page.load(page)

    home_page.go_to_registration_page()
    home_page.register_user(page)

    expect(home_page.account_created_message).to_be_visible()
    expect(home_page.log_out_link).to_be_visible()

    home_page.log_out_link.click()

def test_can_still_login(page: Page):
    # setup
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # test
    page.get_by_text("name=username").fill("bobdylan")
    page.get_by_text("name=password").fill("bobdylan")
    page.get_by_text("value=Log In").click()
   


    # assertion
    expect(page.get_by_text("href=https://parabank.parasoft.com/parabank/logout.htm")).to_be_visible()

    # tear down
    page.get_by_text("href=https://parabank.parasoft.com/parabank/logout.htm").click()