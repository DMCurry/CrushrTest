from playwright.sync_api import Page


class BasePage:
    """Shared behavior for all pages (navigation, common layout)."""

    # Subclasses set this to the path after base_url, e.g. "/login" or ""
    path: str = "/"

    def __init__(self, page: Page, base_url: str = "http://localhost:5173") -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def goto(self) -> None:
        """Navigate to this page."""
        self.page.goto(f"{self.base_url}{self.path}")

    # Shared nav (present on all pages except Login)
    @property
    def nav(self):
        """The main <nav> element."""
        return self.page.locator("nav")

    @property
    def nav_items(self):
        """The 5 <li> links inside nav > ul (one per page)."""
        return self.page.locator("nav ul li")
