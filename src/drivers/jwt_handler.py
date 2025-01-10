import jwt
from datetime import datetime, timedelta, timezone

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key="my_key",
            algorithm="HS256"
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token,
            key="my_key",
            algorithms="HS256"
        )
        return token_information
