from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.TextField()
