from django.db import models
from auth_app.models import User

# Create your models here.


class FeedBack(models.Model):
    title = models.CharField(max_length=100),
   # owner = models.CharField(max_length=50)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
