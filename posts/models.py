from django.db import models
from accounts.models import Account
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=200)
    image = models.ImageField(upload_to='photos/posts',default=None)
    likes = models.IntegerField(default=0)
    location = models.CharField(max_length=80,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
        
class Saved(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Tagged(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tags')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    tagged_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tagged_by')
