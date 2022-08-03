from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView
from .models import BlogPost , Category
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
# Create your views here.

POSTS_PER_PAGE = 2

def search_view(request):
    object_list , search  = _search_posts(request)
    context = {"search": search , 'object_list':object_list,'category': Category.objects.all(),}
    
    return render(request, "blog/search.html",context)


def category_view(request , cats):

    get_object_or_404(Category.objects.filter(id=cats))

    paginator = Paginator(BlogPost.objects.filter(category=cats,published=True),POSTS_PER_PAGE)

    context = {
    'object_list': paginator.get_page(request.GET.get('page')),
    'category': Category.objects.all(),
    
    }

    return render(request, 'blog/category.html', context)

def list_post_view(request):

    paginator = Paginator(BlogPost.objects.filter(published=True),POSTS_PER_PAGE)
    context = {
    'object_list': paginator.get_page(request.GET.get('page')),
    'category': Category.objects.all(),

    }
    return render(request, 'blog/list.html', context)

class DetailPost(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"

def _search_posts(request):

    search = request.POST.get("search")
    # page = request.GET.get("page")
    object_list = BlogPost.objects.filter(published=True)



    if search:
        object_list = object_list.filter(title__icontains=search)
        

    # paginator = Paginator(object_list, POSTS_PER_PAGE)
    # try:
    #     object_list = paginator.page(search)
    # except PageNotAnInteger:
    #     object_list = paginator.page(1)
    # except EmptyPage:
    #     object_list = paginator.page(paginator.num_pages)

    # print("\n \n \n \n \n \n \n ->",object_list.number ,"\n \n \n \n \n \n \n ")

    return object_list , search or ""