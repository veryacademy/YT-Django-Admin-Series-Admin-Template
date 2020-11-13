from django.contrib import admin
from . import models

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.Post)

