from django.shortcuts import render, get_object_or_404
from newsapi import NewsApiClient
from .models import News

def index(request):

    newsapi = NewsApiClient(api_key="d0d74ee48df24d3dbb25dba9c418ae53")
    top = newsapi.get_top_headlines(sources="techcrunch")

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'newsapp/index.html', context={"mylist": mylist})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)

    news.views_count += 1

    if request.method == 'POST':
        if 'like' in request.POST:
            news.likes_count += 1
    elif request.method == 'POST':
        if 'dislike' in request.POST:
            news.dislikes_count += 1

    news.save()