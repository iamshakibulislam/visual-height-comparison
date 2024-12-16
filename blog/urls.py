from django.urls import path
from . import views


urlpatterns = [

path('',views.blog_,name="blog_post")

]