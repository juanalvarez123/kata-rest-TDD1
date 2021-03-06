import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet


class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    public = models.BooleanField(default=False, null=False)


class Object:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
