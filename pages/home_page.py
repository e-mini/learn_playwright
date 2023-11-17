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

    def register_user(self, first_name, last_name, address, city, state, zip_code, phone_number, ssn, user_name, password):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_street_input.fill(address)
        self.address_city_input.fill(city)
        self.customer_address_state.fill(state)
        self.customer_zipCode.fill(zip_code)
        self.customer_phoneNumber.fill(phone_number)
        self.customer_ssn.fill(ssn)
        self.customer_username.fill(user_name)
        self.customer_password.fill(password)
        self.customer_repeated_password.fill(password)
        self.registration_link.click()

    def test_login(self, user_name, password):
        self.test_username.fill(user_name)
        self.test_password.fill(password)
        self.log_in_link.click()












