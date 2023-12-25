from django.db import models


class Dustbin(models.Model):
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dustbin Status: {self.status} at {self.timestamp}"

