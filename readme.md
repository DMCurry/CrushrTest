# Crushr E2E Tests

Playwright + pytest e2e tests for the Crushr application.

## Some useful test commands

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

