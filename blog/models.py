from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import escape
from django.urls import reverse
# Create your models here.

class Category(models.Model):

	name = models.CharField(max_length=60)

	def __str__(self):
		return f"{self.name}"

class BlogPost(models.Model):

	title = models.CharField(max_length=200)
	published = models.BooleanField(default=False)
	content = RichTextField(blank=True , null=True)
	description = models.TextField()

	category = models.ManyToManyField(Category,blank=True)

	def get_absolute_url(self):
		return reverse('detailpost',kwargs={'pk':self.pk})

	# def save(self, *args, **kwargs):
		
		# self.content = escape(self.content)

		# super().save(*args,**kwargs)


	def __str__(self):
		return f"{self.title} | published : {self.published}"