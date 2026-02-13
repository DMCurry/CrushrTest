"""
API client for test data setup (create exercises, performance tests, login, etc.).
Use for arrange step so tests don't depend on UI for creating data.
"""
import os

# TODO: Add HTTP client (requests or httpx). Example shape:
#
# def get_api_base_url() -> str:
#     return os.environ.get("API_BASE_URL", "http://localhost:3000/api")
#
# def login(username: str, password: str) -> dict:
#     """Return tokens or session for storage state."""
#     ...
#
# def create_exercise(token: str, name: str, **kwargs) -> dict:
#     """Create exercise via API; return created resource."""
#     ...
#
# def create_performance_test(token: str, name: str, **kwargs) -> dict:
#     """Create performance test via API."""
#     ...
