from playwright.sync_api import expect
from pages import HomePage, LoginPage
import os


def test_login_redirects_to_home(page, base_url: str) -> None:
    """Log in with test account and verify redirect to home (nav visible)."""

    test_username = os.environ.get("TEST_USER")
    test_password = os.environ.get("TEST_PASSWORD")

    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(test_username, test_password)

    home_page = HomePage(page, base_url)
    expect(home_page.nav).to_be_visible()
    expect(page).to_have_url(home_page.base_url + "/")
