import os
from dotenv import load_dotenv
load_dotenv()


def get_base_url() -> str:
    """App base URL for e2e tests."""
    return os.environ.get("BASE_URL", "http://localhost:5173").rstrip("/")


def get_test_user() -> tuple[str, str]:
    """Test account (username, password). Set TEST_USER and TEST_PASSWORD in env."""
    user = os.environ.get("TEST_USER", "")
    password = os.environ.get("TEST_PASSWORD", "")
    return (user, password)
