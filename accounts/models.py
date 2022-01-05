from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.fields import EmailField
#Automaticaly create a token when user is created
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, real_name, username, email, password=None):
        if not email:
            return ValueError('User must have an email adress')
        if not username:
            return ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            real_name=real_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, real_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            real_name=real_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

DEFAULT ='default_name'
class Account(AbstractBaseUser):
    real_name = models.CharField(max_length=100, default=DEFAULT)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    Description = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='userprofile/')
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'real_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(slef, add_label):
        return True


class UserFollowing(models.Model):
    user = models.ForeignKey(Account, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(Account, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','following_user'],  name="unique_followers")
        ]
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user}"

@receiver(post_save, sender=Account)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
