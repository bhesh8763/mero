from django.db import models

# Create your models here.

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.TextField(blank=True)   
    location = models.CharField(max_length=300, blank=True) 
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}> @ {self.submitted_at:%Y-%m-%d %H:%M}"