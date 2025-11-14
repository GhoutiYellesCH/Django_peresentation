from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True) # Automatically set when created
    
    def __str__(self):
        return self.title
    def article_list(request):
        # ORM query to get all articles, ordered by publication date
        articles = Article.objects.all().order_by('-date_pub') 
        context = {
            'articles': articles,
        }
        return render(request, 'articles_list.html', context)