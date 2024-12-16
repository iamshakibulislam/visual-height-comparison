from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('save-comparison/', views.save_comparison, name='save_comparison'),
    path('blog/',include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

