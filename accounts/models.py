from django.db import models


class Information(models.Model):
    city = models.CharField(max_length=64)
    org = models.CharField(max_length=128)
    user_agent = models.TextField()
    client_ip = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"<Information({self.client_ip})>"

    class Meta:
        ordering = ['-created_at']
