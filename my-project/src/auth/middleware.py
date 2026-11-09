# Authorization 헤더의 Bearer JWT로 사용자를 확인 (실습용)
from auth.jwt_auth import current_user

def check_request(headers):
    auth = headers.get("Authorization", "")
    scheme, _, token = auth.partition(" ")
    if scheme != "Bearer":
        return None
    return current_user(token.strip())
