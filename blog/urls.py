from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home , list_post_view , category_view , DetailPost


urlpatterns = [
    path('home/', home , name="home"),
    path('', list_post_view , name='listposts'),
    path('article/<int:pk>', DetailPost.as_view() , name='detailpost'),
    path('article/category/<int:cats>', category_view , name='listcategory' )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)