from django.test import TestCase
from blog.models import BlogPost
from django.utils import timezone

class TestModel(TestCase):
	
	def setUp(self):
		self.timezone = timezone.now().date()

	def test_blog_model_post_is_create(self):

		blog_post = BlogPost.objects.create(
			title = 'Hello World!',
			content = 'Hello World 2',
			description = 'Hello',
			)

		self.assertEqual(blog_post.published, False)
		# self.assertEquals(blog_post.update_date, self.timezone)
		# self.assertEquals(blog_post.pub_date, self.timezone)