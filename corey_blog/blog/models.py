from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    country=models.CharField(max_length=50,default='india')

    def __str__(self):
        return f"{self.author.username}-{self.country}"
