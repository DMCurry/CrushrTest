from playwright.sync_api import Page
from .base import BasePage


class ExercisesPage(BasePage):
    path = "/exercises"

    def __init__(self, page: Page, base_url: str = "http://localhost:5173") -> None:
        super().__init__(page, base_url)

    # locators (heading, list/grid of exercises, search, add button):
    @property
    def page_heading(self):
        return self.page.get_by_role("heading", name="Exercises")

    @property
    def search_input(self):
        return self.page.get_by_placeholder("Search exercises...")

    @property
    def add_exercise_button(self):
        return self.page.locator(".exercise-add-btn")

    @property
    def exercise_cards(self):
        return self.page.locator(".exercise-details")

    def search(self, query: str) -> None:
        self.search_input.fill(query)

    def click_add_exercise(self) -> None:
        self.add_exercise_button.click()

    def get_exercise_cards(self) -> list[dict]:
        return [
            {
                "name": card.locator("h3").text_content() or "",
                "description": card.get_by_text("Reps").text_content(),
                "category": card.get_by_text("Sets").text_content(),
            }
            for card in self.exercise_cards.all()
        ]
