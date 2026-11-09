# JWT 방식 인증 (access 토큰, HS256)
import os
import time

import jwt

ALGORITHM = "HS256"
DEFAULT_EXPIRES_IN = 3600  # 초


def _secret_key():
    key = os.environ.get("JWT_SECRET")
    if not key:
        raise RuntimeError("환경변수 JWT_SECRET이 설정되지 않았습니다.")
    return key


def login(user_id, expires_in=DEFAULT_EXPIRES_IN):
    now = int(time.time())
    payload = {"sub": user_id, "iat": now, "exp": now + expires_in}
    return jwt.encode(payload, _secret_key(), algorithm=ALGORITHM)


def current_user(token):
    if not token:
        return None
    try:
        payload = jwt.decode(token, _secret_key(), algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        return None
    return payload.get("sub")
