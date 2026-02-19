import pytest
from playwright.sync_api import expect
from pages import HomePage, LoginPage
from utils.config import get_test_user

TEST_USER, TEST_PASSWORD = get_test_user()


def test_schedule_grid_present_on_home(page, base_url: str) -> None:
    """Verify the schedule grid is present on the home page."""
    page.goto(base_url) # Start fresh

    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)
    
    home_page = HomePage(page, base_url)
    #home_page.goto()

    expect(home_page.schedule).to_be_visible(timeout=15_000)


def test_add_exercise_schedule(page, base_url: str) -> None:
    """Make sure exercise shows up after adding it to a certain schedule day"""
    page.goto(base_url) # Start fresh
    
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)

    home_page = HomePage(page, base_url)
    #home_page.goto()

    expect(home_page.schedule).to_be_visible(timeout=15_000)
    home_page.click_add_exercise_on_day("Wednesday")
    home_page.select_workout_plan_in_add_modal("Beginner Strength Training")
    home_page.click_exercise_container_in_add_dropdown("Push-Up")
    assert home_page.has_exercise_on_day("Push-Up", "Wednesday")