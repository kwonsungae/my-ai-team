# 쿠키에 담긴 세션 ID로 사용자를 확인 (실습용)
from auth.session import current_user

def check_request(cookies):
    return current_user(cookies.get("session_id"))
