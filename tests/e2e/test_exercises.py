import pytest
from pages import ExercisesPage, LoginPage

# TODO: Get test credentials from env
TEST_USER = "testuser"
TEST_PASSWORD = "testpass"


@pytest.mark.skip(reason="TODO: implement add-exercise form fill and submit")
def test_add_exercise_appears_after_search(page, base_url: str) -> None:
    """Login -> Visit exercises -> Add exercise -> Search -> Verify card appears."""
    # Login
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)

    # Visit exercises and add a new exercise
    exercises_page = ExercisesPage(page, base_url)
    exercises_page.goto()
    exercises_page.click_add_exercise()

    # TODO: Fill the add-exercise form (modal or inline) and submit.
    # Use a unique name so search is deterministic, e.g. name = "E2E Exercise Unique 123"
    # Then call exercises_page.search(name) and assert the card is in get_exercise_cards().

    exercise_name = "E2E Exercise Unique 123"
    # ... fill form with exercise_name and submit (locators depend on your UI) ...

    exercises_page.search(exercise_name)
    cards = exercises_page.get_exercise_cards()
    names = [c["name"] for c in cards]
    assert exercise_name in names, f"Expected to find {exercise_name} in {names}"
