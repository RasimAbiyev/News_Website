from django.shortcuts import render
from newsapi import NewsApiClient


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