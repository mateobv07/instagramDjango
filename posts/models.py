from django.db import models
from accounts.models import Account
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=200)
    likes = models.IntegerField(default=0)
    location = models.CharField(max_length=80)
    tags = models.ForeignKey(Account, related_name="tagged", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
