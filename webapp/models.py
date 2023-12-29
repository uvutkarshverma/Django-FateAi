from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from datetime import datetime

# url validate if it is https
def validate_https_url(value):
    validator = URLValidator(schemes=['https'])
    try:
        validator(value)
    except ValidationError:
        raise ValidationError('Invalid URL. Please provide a valid HTTPS URL.')


# Create your models here.
class AItools(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=200, validators=[validate_https_url])
    img = models.ImageField(upload_to='static/images/')
    current_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



