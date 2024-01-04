from django.db import models

class DustbinData(models.Model):
    distance = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, default='Pending')  # Set a default value
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"


