# my-project
Claude Code 실습용 작은 파이썬 프로젝트입니다.

## 인증 설정
인증 모듈(`src/auth/jwt_auth.py`)은 JWT(HS256)를 사용하며 서명 키를 환경변수 `JWT_SECRET`에서 읽습니다.

```bash
export JWT_SECRET="충분히-긴-임의의-문자열"
```

`JWT_SECRET`이 없으면 로그인/검증 시 `RuntimeError`가 발생합니다.
