from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model): #To add post into DB via shell ---> post_1 = Post(content = "", title = "", author = ""  ---> post_1.save()
	content = models.TextField()
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
		



