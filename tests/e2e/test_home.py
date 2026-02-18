import pytest
from playwright.sync_api import expect
from pages import HomePage
from utils.config import get_test_user

TEST_USER, TEST_PASSWORD = get_test_user()


@pytest.mark.skip(reason="TODO: implement more checks")
def test_schedule_grid_present_on_home(page, base_url: str) -> None:
    """Verify the schedule grid is present on the home page."""
    home_page = HomePage(page, base_url)
    home_page.goto()
    expect(home_page.schedule).to_be_visible()
