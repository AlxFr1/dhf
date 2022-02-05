from django.contrib import admin

from blog_hillel.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'descript', 'image', 'pub_date', 'is_posted')

