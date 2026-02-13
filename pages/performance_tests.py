from playwright.sync_api import Page
from .base import BasePage


class PerformanceTestsPage(BasePage):
    path = "/performance-tests"

    def __init__(self, page: Page, base_url: str = "http://localhost:3000") -> None:
        super().__init__(page, base_url)

    @property
    def page_heading(self):
        return self.page.get_by_role("heading", name="Performance Tests")

    @property
    def search_input(self):
        return self.page.get_by_placeholder("Search performance tests...")

    @property
    def add_performance_test_button(self):
        return self.page.locator(".performance-test-add-btn")

    @property
    def performance_test_cards(self):
        return self.page.locator(".performance-test-details")

    def search(self, query: str) -> None:
        self.search_input.fill(query)

    def click_add_performance_test(self) -> None:
        self.add_exercise_button.click()

    def get_performance_test_cards(self) -> list[dict]:
        return [
            {
                "name": card.locator("h3").text_content() or "",
                "description": card.get_by_text("Description").text_content(),
                "category": card.get_by_text("Performance Value").text_content(),
            }
            for card in self.exercise_cards.all()
        ]
