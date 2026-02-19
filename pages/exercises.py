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
    def exercise_name_input(self):
        return self.page.locator("input[name='exercise_name']")

    @property
    def exercise_reps_input(self):
        return self.page.locator("input[name='reps']")

    @property
    def exercise_sets_input(self):
        return self.page.locator("input[name='sets']")

    @property
    def exercise_media_link_input(self):
        return self.page.locator("input[name='link']")

    @property
    def exercise_description_input(self):
        return self.page.locator("textarea[name='description']")

    @property
    def exercise_cards(self):
        return self.page.locator(".exercise-details")

    @property
    def exercise_save_button(self):
        return self.page.locator(".save-button")

    def click_add_exercise(self) -> None:
        self.add_exercise_button.click()

    def fill_exercise_name(self, name: str) -> None:
        self.exercise_name_input.fill(name)
    
    def fill_exercise_reps(self, reps: str) -> None:
        self.exercise_reps_input.fill(reps)

    def fill_exercise_sets(self, sets: str) -> None:
        self.exercise_sets_input.fill(sets)

    def fill_exercise_media_link(self, link: str) -> None:
        self.exercise_media_link_input.fill(link)

    def fill_exercise_description(self, description: str) -> None:
        self.exercise_description_input.fill(description)

    def click_save_exercise_button(self) -> None:
        self.exercise_save_button.click()

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
