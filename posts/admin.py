from django.contrib import admin
from .models import Post, Saved, Tagged
# Register your models here.
admin.site.register(Post)
admin.site.register(Saved)
admin.site.register(Tagged)