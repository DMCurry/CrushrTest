from pages import ExercisesPage, LoginPage
from utils.config import get_test_user

TEST_USER, TEST_PASSWORD = get_test_user()


def test_add_exercise_appears_after_search(page, base_url: str) -> None:
    """Login -> Visit exercises -> Add exercise -> Search -> Verify card appears."""
    page.goto(base_url) # Start fresh    

    # Login
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)
    page.wait_for_url(f"{base_url}", timeout=15_000)

    # Visit exercises and add a new exercise
    exercises_page = ExercisesPage(page, base_url)
    exercises_page.nav_exercises_link.click()
    page.wait_for_url(f"{base_url}/exercises", timeout=15_000)
    exercises_page.click_add_exercise()


    exercise_name = "E2E Exercise Unique 123"
    exercises_page.fill_exercise_name(exercise_name)
    exercises_page.fill_exercise_reps("5")
    exercises_page.fill_exercise_sets("3")
    exercises_page.fill_exercise_media_link("https://www.youtube.com/shorts/omG6jR4nuIs")
    exercises_page.fill_exercise_description("Olympic Training Exercise (Planet Fitness Edition)")
    exercises_page.click_save_exercise_button()

    exercises_page.search(exercise_name)
    cards = exercises_page.get_exercise_cards()
    names = [c["name"] for c in cards]
    assert exercise_name in names, f"Expected to find {exercise_name} in {names}"
