from playwright.sync_api import expect
from pages import HomePage, LoginPage
from utils.config import get_test_user

TEST_USER, TEST_PASSWORD = get_test_user()


def test_login_redirects_to_home(page, base_url: str) -> None:
    """Log in with test account and verify redirect to home (nav visible)."""

    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)

    home_page = HomePage(page, base_url)
    expect(home_page.nav).to_be_visible()
    expect(page).to_have_url(home_page.base_url + "/")
