from playwright.sync_api import Page
from .base import BasePage


class HomePage(BasePage):
    path = "/"

    def __init__(self, page: Page, base_url: str = "http://localhost:5173") -> None:
        super().__init__(page, base_url)

    @property
    def schedule(self):
        return self.page.locator(".calendar-grid")
    
    @property
    def schedule_save_button(self):
        return self.page.get_by_label("Save Schedule")

    def save_schedule(self) -> None:
        self.schedule_save_button.click()

    # TODO: Add locators and actions for the graphs