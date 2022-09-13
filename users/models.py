# 기존 user 모델 호출
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREA = "kr"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREA, "Korea"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    avator = models.ImageField(
        upload_to="avatars", blank=True
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=GENDER_MALE,
        max_length=10,
        # null=True,  # 비어있는 필드
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    birthday = models.DateField(
        blank=True,
        null=True
    )

    language = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True
    )

    currency = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True
    )

    superhost = models.BooleanField(default=False)
