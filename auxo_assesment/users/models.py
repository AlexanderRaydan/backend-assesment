""" User models """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Models
from auxo_assesment.models import AuxoAssesmentModel


class User(AuxoAssesmentModel, AbstractUser):
    """User model """

    email = models.EmailField(
        'email address',
        unique=True,
        null=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
