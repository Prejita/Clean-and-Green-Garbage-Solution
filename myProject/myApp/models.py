from django.db import models

class DustbinData(models.Model):
    fill_percentage = models.FloatField()
    is_filled = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dustbin data: {self.fill_percentage}% Filled ({self.timestamp})"
