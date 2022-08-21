from django.test import TestCase
from blog.models import BlogPost

class TestModel(TestCase):
		
	def test_blog_model_post_is_create(self):

		blog_post = BlogPost.objects.create(
			title = 'Hello World!',
			content = 'Hello World 2',
			description = 'Hello',
			)

		self.assertEqual(blog_post.published, False)