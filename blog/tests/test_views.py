from django.test import TestCase , Client
from django.urls import reverse
from blog.views import list_post_view , category_view , DetailPost , search_view
from blog.models import BlogPost , Category
class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.list_url = reverse('listposts')
		self.detail_url = reverse('detailpost',args=[1])
		self.search_url = reverse('search-bar')
		self.category_url = reverse('listcategory',args=[1])

		self.blog_category = Category.objects.create(
			name='sirehassan',
			)

		self.blog_post = BlogPost.objects.create(
			title = 'Hello World!',
			published = True,
			content = 'Hello World 2',
			description = 'Hello',

			)
	
	def test_blog_list_get(self):

		response = self.client.get(self.list_url)

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'blog/list.html')
		self.assertEquals(response.context['object_list'].number, response.context['object_list'].paginator.page(1).number)

	def test_blog_search_get(self):

		response = self.client.get(self.search_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed('blog/search')

	def test_blog_detail_get(self):

		response = self.client.get(self.detail_url)

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'blog/detail.html')

	def test_blog_category_get(self):

		response = self.client.get(self.category_url)
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response, 'blog/category.html')