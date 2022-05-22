from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.TextField()
    ip = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip

    class Meta:
        ordering = ['-created']
