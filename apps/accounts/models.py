from django.contrib.auth.models import AbstractUser


# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#substituting-a-custom-user-model
class User(AbstractUser):
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
