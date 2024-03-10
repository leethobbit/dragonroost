import jwt
from django.conf import settings
from ninja.security import HttpBearer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class JWTAuth(HttpBearer):
    """
    Currently not in use!!!!
    """
    def authenticate(self, request, token):
        try:
            # Decode the JWT token
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])

            # Get user info from token payload
            user = get_user_model().objects.get(id=payload["id"])
            return user, token
        except Exception as e:
            return None
        
