from playwright.sync_api import Page
from .base import BasePage


class HomePage(BasePage):
    path = "/"

    def __init__(self, page: Page, base_url: str = "http://localhost:5173") -> None:
        super().__init__(page, base_url)

    # --- Schedule grid (calendar-grid > calendar-day, each with h3, add-exercise-btn, exercise-container, performance-test-container) ---
    @property
    def schedule(self):
        return self.page.locator(".calendar-grid")

    @property
    def calendar_days(self):
        return self.page.locator(".calendar-day")

    @property
    def schedule_save_button(self):
        return self.page.locator(".save-schedule-btn")

    @property
    def add_exercise_buttons(self):
        return self.page.locator(".add-exercise-btn")

    @property
    def select_workout_plan_dropdown(self):
        return self.page.locator(".dropdown-container").locator(".custom-select")

    @property
    def add_modal_workout_plan_select(self):
        """Select in the add-modal's dropdown-container (e.g. 'Beginner Strength Training')."""
        return self.page.locator(".add-modal").locator(".dropdown-container").locator("select")

    # --- Result submission (modal/form after clicking a performance test; adjust selectors to match your UI) ---
    @property
    def performance_test_result_input(self):
        # Scope to dialog/modal then input (adjust first locator if your modal uses a different selector)
        return self.page.locator("[role='dialog']").locator("input[name='result'], input[name='value']").first

    @property
    def performance_test_result_submit_button(self):
        return self.page.get_by_role("button", name="Submit")

    # --- Graphs (graph-container with h3 per test name, recharts) ---
    @property
    def graph_containers(self):
        return self.page.locator(".graph-container")

    # --- Methods ---
    def _day_locator(self, day_name: str):
        """Calendar day that has an h3 with this day name (e.g. 'Monday')."""
        return self.page.locator(".calendar-day").filter(has=self.page.get_by_role("heading", name=day_name))

    def click_add_exercise_on_day(self, day_name: str) -> None:
        """Click the add-exercise button for the given day (e.g. 'Monday')."""
        self._day_locator(day_name).locator(".add-exercise-btn").click()

    def select_workout_plan_in_add_modal(self, plan_name_label: str) -> None:
        """Select 'Beginner Strength Training' from the add-modal's workout plan dropdown."""
        self.add_modal_workout_plan_select.select_option(label=plan_name_label)

    def click_exercise_container_in_add_dropdown(self, exercise_name: str) -> None:
        """Click the exercise container that contains this exercise name (e.g. 'Push-Up')."""
        self.page.locator(".exercise-container").filter(has_text=exercise_name).click()

    def has_exercise_on_day(self, exercise_name: str, day_name: str) -> bool:
        """Return True if the given day's exercise-container shows this exercise name."""
        day = self._day_locator(day_name)
        container = day.locator(".exercise-container").filter(has_text=exercise_name)
        return container.count() > 0

    def click_performance_test_on_day(self, test_name: str, day_name: str) -> None:
        """Click the performance test (e.g. 'Strength Test') inside the given day's performance-test-container."""
        day = self._day_locator(day_name)
        day.locator(".performance-test-container").filter(has_text=test_name).click()

    def fill_performance_test_result(self, value: str) -> None:
        self.performance_test_result_input.fill(value)

    def click_submit_performance_test_result(self) -> None:
        self.performance_test_result_submit_button.click()

    def save_schedule(self) -> None:
        self.schedule_save_button.click()