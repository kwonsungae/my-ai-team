# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Dependencies (no lockfile or pyproject; plain requirements file):
```bash
python3 -m pip install -r requirements.txt   # pytest, PyJWT
```

Run all tests:
```bash
python3 -m pytest
```

Run one test file or one test:
```bash
python3 -m pytest tests/test_auth.py
python3 -m pytest tests/test_auth.py::test_expired_token_rejected
```

No linter or formatter is configured.

Auth tests set `JWT_SECRET` themselves via an autouse fixture, so they need no environment setup. Anything that calls `login()` outside tests requires `JWT_SECRET` in the environment, otherwise it raises `RuntimeError`.

## Architecture

Small Python project with no web framework and no packaging config. Code lives in `src/` and tests in `tests/`.

Tests import modules by inserting `src/` into `sys.path` at the top of each test file. There is no `conftest.py` or package install, so new tests should follow the same pattern.

**Auth (`src/auth/`)** is the only substantive subsystem:
- `jwt_auth.py` issues and verifies HS256 access tokens with PyJWT. `login(user_id)` returns a token; `current_user(token)` returns the `sub` claim or `None` for missing, expired, forged or malformed tokens. The signing key comes from the `JWT_SECRET` environment variable and is never hardcoded.
- `middleware.py` `check_request(headers)` reads `Authorization: Bearer <token>` and delegates to `current_user`. It returns `None` for any other scheme and does not reject requests itself; callers decide what to do with `None`.
- Nothing in `src/main.py` or `src/utils.py` imports `auth`, so the auth module is not wired into any entry point yet.
- There is no logout, signup, password check or server-side token revocation. Logout would be client-side token disposal only.

**`src/main.py`** is a stub: `greet()` prints a greeting, and `greet("world")` is called at module import time, so importing `main` prints output.

`src/utils.py` contains a single `add` function and is not used elsewhere.
