import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from faker import Faker

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



# building blocks

# able to code in programming language
# able to use test runner
# able
    # test should always host the test data
    # assertions should always be in the test


