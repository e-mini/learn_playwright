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
def test_can_register(page: Page):
    faker = Faker()
    first_name = faker.name().split(" ")[0]
    last_name = faker.name().split(" ")[1]
    address = faker.address().split("\n")[0]
    city = faker.city()
    state = faker.state()
    zip_code = faker.zipcode()
    phone_number = faker.phone_number()
    ssn = faker.ssn()
    user_name = faker.user_name() + faker.zipcode()
    password = faker.word()

    home_page = HomePage(page)
    home_page.load(page)

    home_page.go_to_registration_page()
    home_page.register_user(first_name, last_name, address, city, state, zip_code, phone_number, ssn, user_name, password)

    expect(home_page.account_created_message).to_be_visible()
    expect(home_page.log_out_link).to_be_visible()

    home_page.log_out_link.click()

def test_can_still_login(page: Page):
    # create test data
    faker = Faker()
    first_name = faker.name().split(" ")[0]
    last_name = faker.name().split(" ")[1]
    address = faker.address().split("\n")[0]
    city = faker.city()
    state = faker.state()
    zip_code = faker.zipcode()
    phone_number = faker.phone_number()
    ssn = faker.ssn()
    user_name = faker.user_name() + faker.zipcode()
    password = faker.word()
    home_page = HomePage(page)
    home_page.load(page)
    home_page.go_to_registration_page()
    home_page.register_user(first_name, last_name, address, city, state, zip_code, phone_number, ssn, user_name,
                            password)
    home_page.log_out_link.click()

    # actual test logging in begins
    home_page.test_login(user_name, password)
    expect(home_page.log_out_link).to_be_visible()

    home_page.log_out_link.click()


# building blocks

# able to code in programming language
# able to use test runner
# able
    # test should always host the test data
    # assertions should always be in the test


