from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):

	name = models.CharField(max_length=60)

	def __str__(self):
		return f"{self.name}"

class BlogPost(models.Model):

	title = models.CharField(max_length=200)
	published = models.BooleanField(default=False)
	pub_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)
	content = RichTextField(blank=True , null=True)
	description = models.TextField()


	category = models.ManyToManyField(Category,blank=True)

	def get_absolute_url(self):
		return reverse('detailpost',kwargs={'pk':self.pk})
	
	def save(self, *args, **kwargs):

		if self.published == True:
			self.update_date = timezone.now()

		super(BlogPost, self).save(*args, **kwargs)


	def __str__(self):
		return f"{self.title} | published : {self.published} | pup : {self.pub_date} | update : {self.update_date} "