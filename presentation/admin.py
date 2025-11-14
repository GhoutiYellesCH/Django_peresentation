from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_pub') # Display these fields in the admin list
    list_filter = ('date_pub',)
    search_fields = ('title', 'content')
