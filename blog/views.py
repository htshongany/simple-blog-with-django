from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import BlogPost , Category
from django.core.paginator import Paginator
# Create your views here.

# def home(request):
# 	context = {
# 	'posts':BlogPost.objects.all(),
# 	'category': Category.objects.all()
# 	}

# 	return render(request, 'home.html', context)

def category_view(request , cats):

	get_object_or_404(Category.objects.filter(id=cats))

	paginator = Paginator(BlogPost.objects.filter(category=cats,published=True),2)

	context = {
	'object_list': paginator.get_page(request.GET.get('page')),
	'category': Category.objects.all(),
	
	}

	return render(request, 'blog/category.html', context)

def list_post_view(request):

	paginator = Paginator(BlogPost.objects.filter(published=True),2)
	context = {
	'object_list': paginator.get_page(request.GET.get('page')),
	'category': Category.objects.all(),

	}
	return render(request, 'blog/list.html', context)


class DetailPost(DetailView):
	model = BlogPost
	template_name = "blog/detail.html"
