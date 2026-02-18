from playwright.sync_api import Page
from .base import BasePage


class LoginPage(BasePage):
    path = "/login"

    def __init__(self, page: Page, base_url: str = "http://localhost:5173") -> None:
        super().__init__(page, base_url)

    @property
    def email_input(self):
        return self.page.locator("form input[type='text']")
    
    @property
    def password_input(self):
        return self.page.locator("form input[type='password']")
    
    @property
    def submit_button(self):
        return self.page.get_by_role("button", name="Login")

    def fill_credentials(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        print(email)
        self.password_input.fill(password)
    
    def submit(self) -> None:
        self.submit_button.click()
    
    def login(self, email: str, password: str) -> None:
        self.fill_credentials(email, password)
        self.submit()
