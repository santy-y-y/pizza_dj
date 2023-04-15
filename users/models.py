from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

def _phone_validate(phone):
        if not phone.isdigit():
            raise ValidationError(
                _("%(phone)s is not a string of digits"),
                params={'value': phone}
            )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(10, 'phone number shold has at least 10 digits'),
            MaxLengthValidator(10, 'phone number should has no more than 10 digits'),
            _phone_validate
        ]
        )
        
