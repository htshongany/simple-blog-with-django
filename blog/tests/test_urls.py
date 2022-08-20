from django.test import TestCase , SimpleTestCase
from blog.views import list_post_view , category_view , DetailPost , search_view
from django.urls import reverse , resolve 

# Create your tests here.

class TestUrls(SimpleTestCase):

	def test_list_post_url_is_resolved(self):

		url = reverse('listposts')
		self.assertEquals(resolve(url).func , list_post_view)

	def test_search_url_is_resolved(self):

		url = reverse('search-bar')
		self.assertEquals(resolve(url).func , search_view)

	def test_category_url_is_resolved(self):

		url = reverse('listcategory', args=[1])
		self.assertEquals(resolve(url).func , category_view)

	def test_DetailPost_url_is_resolved(self):

		url = reverse('detailpost', args=[1])
		self.assertEquals(resolve(url).func.view_class , DetailPost)