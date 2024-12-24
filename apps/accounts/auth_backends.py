from typing import Optional

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser


# https://docs.djangoproject.com/en/5.1/ref/settings/#authentication-backends
class EmailAuthBackend(BaseBackend):
    def get_user(self, user_id: int) -> Optional[settings.AUTH_USER_MODEL]:
        UserModel: AbstractUser = get_user_model()
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None

    def authenticate(
        self, request, username: str = None, password: str = None
    ) -> Optional[settings.AUTH_USER_MODEL]:
        UserModel: AbstractUser = get_user_model()
        email = username.lower()
        if not email:
            return None
        try:
            user = UserModel.objects.get(email__iexact=email)
            if user and check_password(password, user.password):
                return user
            return None
        except UserModel.DoesNotExist:
            return None
