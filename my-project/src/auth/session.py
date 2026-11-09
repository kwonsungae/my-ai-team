# 세션 방식 인증 (실습용)
SESSIONS = {}

def login(user_id):
    session_id = "sess-" + user_id
    SESSIONS[session_id] = user_id
    return session_id

def current_user(session_id):
    return SESSIONS.get(session_id)
