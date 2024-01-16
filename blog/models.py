from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=255)
	content = FroalaField()
	date = models.DateField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	featured = models.BooleanField(default=False)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)