from django.db import models

class DustbinStatus(models.Model):
    # Your fields here
    status = models.CharField(max_length=50)  # For example

    def __str__(self):
        return self.status  # Adjust this according to your model
