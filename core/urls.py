from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('', include('blog.urls', namespace='blog')),
] + staticfiles_urlpatterns()



