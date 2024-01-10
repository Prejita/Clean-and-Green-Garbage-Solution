# from django.db import models

# class DustbinData(models.Model):
#     distance = models.FloatField(default=0.0)
#     status = models.CharField(max_length=10, default='Pending')
#     kathmandu_time = models.DateTimeField(null=True, blank=True)  # Add a new field for Kathmandu time
#     timestamp = models.DateTimeField(auto_now_add=True)
#     location = models.CharField(max_length=100, default='Null')

#     def __str__(self):
#         return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"

from django.db import models

class DustbinData(models.Model):
    distance = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, default='Pending')
    kathmandu_time = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, default='Null')

    def save(self, *args, **kwargs):
        # Check if the status is 'Full', create a notification if it is
        if self.status == 'Full':
            Notification.objects.create(
                message="The dustbin is full",
                location=self.location,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"

class Notification(models.Model):
    message = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} at {self.location} - {self.timestamp}"
