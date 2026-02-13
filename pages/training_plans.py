from playwright.sync_api import Page, Locator
from .base import BasePage


class TrainingPlansPage(BasePage):
    path = "/training-plans"

    def __init__(self, page: Page, base_url: str = "http://localhost:5713") -> None:
        super().__init__(page, base_url)

    @property
    def dropdown_options(self):
        return self.page.locator(".dropdown-container").locator("select").locator("option")

    @property
    def add_training_plan_button(self):
        return self.page.locator(".training-plan-add-btn")

    def click_add_training_plan(self) -> None:
        self.add_training_plan_button.click()

    def get_training_plan_options(self) -> list[Locator]:
        return self.dropdown_options.all()

    # TODO: Add more locators and actions for the training plan details