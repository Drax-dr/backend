from django.db import models


class Assignments(models.Model):
        assignID  =  models.CharField(max_length=6, name="ID")
        created_at = models.DateTimeField(default=now)