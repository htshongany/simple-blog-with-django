from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import BlogPost
# Create your views here.

def home(request):
	context = {}
	return render(request, 'base.html', context)

class ListPosts(ListView):
	model = BlogPost
	template_name = "list.html"

class DetailPost(DetailView):
	model = BlogPost
	template_name = "detail.html"
