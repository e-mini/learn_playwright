import pytest
from faker import Faker
from pages.home_page import HomePage


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
    return {"first_name": first_name, "last_name": last_name, "address": address,
            "city": city, "state": state, "zip_code": zip_code, "phone_number": phone_number,
            "ssn": ssn, "user_name": user_name, "password": password}



