
from django.shortcuts import render, get_object_or_404
from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news': news, 
        'title': 'НОВОСТИ',
        }
    return render(request, "new/index.html", context)
    
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news, 
        'category': category,
        }
    return render(request, "new/category.html", context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'new/view_news.html', {'news_item': news_item})
