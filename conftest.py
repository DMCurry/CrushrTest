import os
import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """App base URL. Set BASE_URL env var or defaults to localhost."""
    return os.environ.get("BASE_URL", "http://localhost:5173")


# TODO: Add a fixture that logs in and yields page (or storage state) so tests
# can use it and skip the login step, e.g.:
# @pytest.fixture
# def logged_in_page(page, base_url):
#     from pages import LoginPage, HomePage
#     login_page = LoginPage(page, base_url)
#     login_page.goto()
#     login_page.login(os.environ["TEST_USER"], os.environ["TEST_PASSWORD"])
#     expect(HomePage(page, base_url).nav).to_be_visible()
#     return page
