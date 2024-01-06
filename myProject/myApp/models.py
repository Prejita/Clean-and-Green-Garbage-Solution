# from django.db import models

# class DustbinData(models.Model):
#     distance = models.FloatField(default=0.0)
#     status = models.CharField(max_length=10, default='Pending')  # Set a default value
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"

# from django.db import models

# class DustbinData(models.Model):
#     distance = models.FloatField(default=0.0)
#     status = models.CharField(max_length=10, default='Pending')
#     kathmandu_time = models.DateTimeField(null=True, blank=True)  # Add a new field for Kathmandu time
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"

from django.db import models

class DustbinData(models.Model):
    distance = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, default='Pending')
    kathmandu_time = models.DateTimeField(null=True, blank=True)  # Add a new field for Kathmandu time
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, default='Null')

    def __str__(self):
        return f"Dustbin data: {self.distance} cm, Status: {self.status} ({self.timestamp})"
