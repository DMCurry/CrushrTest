# Crushr E2E Tests

Playwright + pytest e2e tests for the Crushr application.

## Prerequisites

- Python venv activated
- `pip install -r requirements.txt`
- `playwright install` (browsers)
- App running at `BASE_URL` (default `http://localhost:5173`)
- `.env` with `TEST_USER`, `TEST_PASSWORD` (and optionally `BASE_URL`), or use `python-dotenv` and `load_dotenv()` in `conftest.py`

## Test commands

**Run all e2e tests (headless, non-debug)**  
```bash
pytest tests/e2e -v
```

**Run a single test file**  
```bash
pytest tests/e2e/test_home.py -v
pytest tests/e2e/test_performance_tests.py -v
```

**Run with print output visible**  
```bash
pytest tests/e2e -v -s
```

**Run in headed mode (see the browser)**  
```bash
pytest tests/e2e -v --headed
```

**Run in debug mode (headed + Playwright Inspector + slow)**  
```bash
PWDEBUG=1 pytest tests/e2e/test_performance_tests.py -v
```

