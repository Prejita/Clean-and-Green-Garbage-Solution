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
    

# class Event(models.Model):
#     name = models.CharField(max_length=255)
#     organizer = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     location = models.CharField(max_length=255)
#     category_choices = [
#         ('Conference', 'Conference'),
#         ('Seminar', 'Seminar'),
#         ('Workshop', 'Workshop'),
#         ('Clean-up Campaigns', 'Clean-up Campaigns'),
#         ('Tree-planting Drives', 'Tree-planting Drives'),
#         ('Others', 'Others'),
#     ]
#     category = models.CharField(max_length=20, choices=category_choices)
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.name} ({self.start_date} to {self.end_date})"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(null="True", max_length=50)  
    end_time = models.CharField(null="True", max_length=50) 
    location = models.CharField(max_length=255)
    category_choices = [
        ('Conference', 'Conference'),
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Clean-up Campaigns', 'Clean-up Campaigns'),
        ('Tree-planting Drives', 'Tree-planting Drives'),
        ('Others', 'Others'),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.start_date} {self.start_time} to {self.end_date} {self.end_time})"
