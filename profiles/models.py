from django.db import models
from django.contrib.auth.models import User

class AbstractProfile(models.Model):
    user = models.ForeignKey(User, rel)
