from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home , ListPosts , DetailPost , category_view


urlpatterns = [
    path('home/', home , name="home"),
    path('', ListPosts.as_view() , name='listposts'),
    path('article/<int:pk>', DetailPost.as_view() , name='detailpost'),
    path('article/category/<int:cats>', category_view , name='listcategory' )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)