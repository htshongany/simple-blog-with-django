from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import BlogPost , Category
from django.core.paginator import Paginator
# Create your views here.

def home(request):
	context = {
	'posts':BlogPost.objects.all(),
	'category': Category.objects.all()

	}

	return render(request, 'home.html', context)

def category_view(request , cats):

	get_object_or_404(Category.objects.filter(id=cats))

	paginator = Paginator(BlogPost.objects.filter(category=cats),2)

	context = {
	'page_obj': paginator.get_page(request.GET.get('page'))	

	}



	return render(request, 'category.html', context)

class ListPosts(ListView):
	model = BlogPost
	paginate_by = 2
	template_name = "list.html"

class DetailPost(DetailView):
	model = BlogPost
	template_name = "detail.html"
