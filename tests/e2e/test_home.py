from playwright.sync_api import expect
from pages import HomePage


def test_schedule_grid_present_on_home(page, base_url: str) -> None:
    """Verify the schedule grid is present on the home page."""
    home_page = HomePage(page, base_url)
    home_page.goto()
    expect(home_page.schedule).to_be_visible()
