import re
from playwright.sync_api import Page, expect

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
    # setup
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # test
    page.get_by_text("Register").click()
    register_user(page)


    # assertion
    expect(page.get_by_text("Your account was created successfully. You are now logged in.")).to_be_visible()
    expect(page.get_by_text("Log Out")).to_be_visible()
    # tear down
    page.get_by_text("Log Out").click()
def register_user(page: Page ):
    page.locator('input[name="customer.firstName"]').fill("Robin")
    page.locator('input[name="customer.lastName"]').fill("Sample")
    page.locator('input[name="customer.address.street"]').fill("123 Main St.")
    page.locator('input[name="customer.address.city"]').fill("Atlanta")
    page.locator('input[name="customer.address.state"]').fill("Georgia")
    page.locator('input[name="customer.address.zipCode"]').fill("30324")
    page.locator('input[name="customer.phoneNumber"]').fill("(123)456-7890")
    page.locator('input[name="customer.ssn"]').fill("123-456-7890")
    page.locator('input[name="customer.username"]').fill("robinsam")
    page.locator('input[name="customer.password"]').fill("sampley")
    page.locator("#repeatedPassword").fill("sampley")
    page.locator('input[value="Register"]').click()


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