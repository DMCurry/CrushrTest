import pytest
from pages import LoginPage, PerformanceTestsPage

# TODO: Get test credentials from env
TEST_USER = "testuser"
TEST_PASSWORD = "testpass"


@pytest.mark.skip(reason="TODO: implement add-performance-test form fill and submit")
def test_add_performance_test_appears_after_search(page, base_url: str) -> None:
    """Login -> Visit performance tests -> Add performance test -> Search -> Verify card."""
    # Login
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)

    # Visit performance tests and add one
    perf_page = PerformanceTestsPage(page, base_url)
    perf_page.goto()
    perf_page.click_add_performance_test()

    # TODO: Fill the add-performance-test form and submit.
    # Use a unique name, e.g. "E2E Perf Test Unique 456", then search and verify.

    test_name = "E2E Perf Test Unique 456"
    # ... fill form and submit (locators depend on your UI) ...

    perf_page.search(test_name)
    cards = perf_page.get_performance_test_cards()
    names = [c["name"] for c in cards]
    assert test_name in names, f"Expected to find {test_name} in {names}"
