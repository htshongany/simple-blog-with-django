from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import BlogPost , Category
# Create your views here.

def home(request):
	context = {
	'posts':BlogPost.objects.all(),
	'category': Category.objects.all()

	}

	return render(request, 'home.html', context)

class ListPosts(ListView):
	model = BlogPost
	paginate_by = 2
	template_name = "list.html"

class DetailPost(DetailView):
	model = BlogPost
	template_name = "detail.html"
