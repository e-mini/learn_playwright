from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from faker import Faker
import pytest


# class TestAuthentication(Page):
def test_can_register(page, create_user):
    home_page = HomePage(page)
    expect(home_page.account_created_message).to_be_visible()
    expect(home_page.log_out_link).to_be_visible()


def test_can_still_login(page: Page, create_user):
    created_user_object = create_user
    home_page = HomePage(page)
    home_page.load(page)
    home_page.test_login(created_user_object["user_name"], created_user_object["password"])
    expect(home_page.log_out_link).to_be_visible()

    home_page.log_out_link.click()

@pytest.fixture
def create_fake_user_data():
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
    return { "first_name": first_name, "last_name": last_name, "address": address,
     "city": city, "state": state, "zip_code": zip_code, "phone_number": phone_number,
     "ssn": ssn, "user_name": user_name, "password": password }

@pytest.fixture
def create_user(page, create_fake_user_data):
    home_page = HomePage(page)
    home_page.load(page)
    home_page.go_to_registration_page()
    home_page.register_user(create_fake_user_data["first_name"], create_fake_user_data["last_name"],
                            create_fake_user_data["address"],
                            create_fake_user_data["city"], create_fake_user_data["state"],
                            create_fake_user_data["zip_code"],
                            create_fake_user_data["phone_number"], create_fake_user_data["ssn"],
                            create_fake_user_data["user_name"],
                            create_fake_user_data["password"])
    home_page.log_out_link.click()
    return create_fake_user_data