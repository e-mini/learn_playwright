from playwright.sync_api import Page


class HomePage:
    base_url = "https://parabank.parasoft.com/parabank"


    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator('input[name="customer.firstName"]')
        self.last_name_input = page.locator('input[name="customer.lastName"]')
        self.address_street_input = page.locator('input[name="customer.address.street"]')
        self.address_city_input = page.locator('input[name="customer.address.city"]')
        self.customer_address_state = page.locator('input[name="customer.address.state"]')
        self.customer_zipCode = page.locator('input[name="customer.address.zipCode"]')
        self.customer_phoneNumber = page.locator('input[name="customer.phoneNumber"]')
        self.customer_ssn = page.locator('input[name="customer.ssn"]')
        self.customer_username = page.locator('input[name="customer.username"]')
        self.customer_password = page.locator('input[name="customer.password"]')
        self.customer_repeated_password = page.locator("#repeatedPassword")
        self.registration_link = page.locator('input[value="Register"]')
        self.account_created_message = page.get_by_text("Your account was created successfully. You are now logged in.")
        self.register_link = page.get_by_text("Register")
        self.log_out_link = page.get_by_text("Log Out")
        self.test_username = page.locator('input[name="username"]')
        self.test_password = page.locator('input[name="password"]')
        self.log_in_link = page.locator('input[value="Log In"]')




    def load(self, page):
        page.goto(self.base_url + "/index.htm")

    def go_to_registration_page(self):
        self.register_link.click()

    def register_user(self, page):
        self.first_name_input.fill("Robin")
        self.last_name_input.fill("Sample")
        self.address_street_input.fill("123 Main St.")
        self.address_city_input.fill("Atlanta")
        self.customer_address_state.fill("Georgia")
        self.customer_zipCode.fill("30324")
        self.customer_phoneNumber.fill("(123) 456-7890")
        self.customer_ssn.fill("123-456-7890")
        self.customer_username.fill("robinsam")
        self.customer_password.fill("sampley")
        self.customer_repeated_password.fill("sampley")
        self.registration_link.click()

    def test_registration(self, page):
        self.test_username.fill("bobdylan")
        self.test_password.fill("bobdylan")
        self.log_in_link.click()













