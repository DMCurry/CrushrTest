import pytest
from pages import LoginPage, PerformanceTestsPage
from utils.config import get_test_user

TEST_USER, TEST_PASSWORD = get_test_user()


def test_add_performance_test_appears_after_search(page, base_url: str) -> None:
    """Login -> Visit performance tests -> Add performance test -> Search -> Verify card."""
    page.goto(base_url) # Start fresh    

    # Login
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login(TEST_USER, TEST_PASSWORD)
    page.wait_for_url(f"{base_url}", timeout=15_000)

    # Visit performance tests and add one
    perf_page = PerformanceTestsPage(page, base_url)
    perf_page.nav_performance_tests_link.click()
    page.wait_for_url(f"{base_url}/performance-tests", timeout=15_000)    
    perf_page.click_add_performance_test()

    test_name = "E2E Perf Test Unique 456"
    perf_page.fill_performance_test_name(test_name)
    perf_page.fill_performance_test_description("E2E Performance Test Description 456")
    perf_page.click_save_performance_test()

    perf_page.search(test_name)
    cards = perf_page.get_performance_test_cards()
    names = [c["name"] for c in cards]
    assert test_name in names, f"Expected to find {test_name} in {names}"
