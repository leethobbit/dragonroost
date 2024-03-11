import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

def issue_jwt_token(user: AbstractUser) -> str:
    payload = {
        "id": user.id,
        "exp": datetime.utcnow() + timedelta(days=1) # The token will expire in 1 day
        }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")
    return token