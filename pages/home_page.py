from playwright.sync_api import Page


class HomePage:
    base_url = "https://parabank.parasoft.com/parabank"


    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator('input[name="customer.firstName"]')
        self.last_name_input = page.locator('input[name="customer.lastName"]')
        self.account_created_message = page.get_by_text("Your account was created successfully. You are now logged in.")
        self.register_link = page.get_by_text("Register")
        self.log_out_link = page.get_by_text("Log Out")


    def load(self, page):
        page.goto(self.base_url + "/index.htm")

    def go_to_registration_page(self):
        self.register_link.click()

    def register_user(self, page):
        self.first_name_input.fill("Robin")
        self.last_name_input.fill("Sample")
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

