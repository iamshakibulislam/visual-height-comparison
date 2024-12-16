from django.urls import path
from . import views


urlpatterns = [

path('<str:slug>',views.blog_,name="blog_post")

]