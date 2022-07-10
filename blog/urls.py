from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home , ListPosts , DetailPost 


urlpatterns = [
    path('home/', home , name="home"),
    path('', ListPosts.as_view() , name='listposts'),
    path('article/<int:pk>', DetailPost.as_view() , name='detailpost'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)