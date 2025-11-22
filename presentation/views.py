from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import JsonResponse # for the API usage
from django.core import serializers
import json
from datetime import datetime

def home(request):
    return render(request, 'index.html')

def mvt(request):
    return render(request, 'mvt.html')

def orm(request):
    return render(request, 'orm.html')

def templates_demo(request):
    return render(request, 'templates.html')

def security(request):
    return render(request, 'security.html')

@login_required
def dashboard(request):
    total_articles = Article.objects.count()
    last_article = Article.objects.order_by('-date_pub').first()
    recent_articles = Article.objects.order_by('-date_pub')[:5] # Bonus: Last 5 articles
    
    context = {
        'total_articles': total_articles,
        'last_article': last_article,
        'recent_articles': recent_articles,
        'user_count': len(request.user.get_all_permissions()),
    }
    return render(request, 'dashboard.html', context)

def api_intro(request):
    return render(request, 'api_intro.html')

def conclusion(request):
    return render(request, 'conclusion.html')

def article_list(request):
    articles = Article.objects.all().order_by('-date_pub') 
    context = {
        'articles': articles,
    }
    return render(request, 'articles_list.html', context)

def api_articles(request):
    articles = Article.objects.all().order_by('-date_pub')
    data = list(articles.values('title', 'date_pub'))
    return JsonResponse(data, safe=False)

def api_stats(request):
    total_articles = Article.objects.count()
    last_pub = Article.objects.order_by('-date_pub').values_list('date_pub', flat=True).first()
    
    stats = {
        'total_articles': total_articles,
        'last_pub_date': last_pub.strftime('%Y-%m-%d %H:%M:%S') if last_pub else 'N/A',
        'status': 'OK',
    }
    return JsonResponse(stats)