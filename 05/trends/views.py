from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from .models import Keyword, Trend
from .forms import KeywordForm
from io import BytesIO
import matplotlib.pyplot as plt
import base64
import pandas as pd

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = KeywordForm()
    context = {
        'keywords': keywords,
        'form': form,
    }
    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()
    trendlist = Trend.objects.values_list('name', flat=True)

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword}'
        
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search = soup.select_one('.LHJvCe')
        search = str(search).replace(',', '')
        search = str(search).split('검색결과 약 ')
        search = search[1]
        search = str(search).split('개')
        search = search[0]
        
        if keyword.name not in trendlist:
            trend = Trend.objects.create(name=keyword.name, result=search, search_period='all')
        else:
            trend = Trend.objects.get(name=keyword.name)
            trend.result = search
            trend.save()

    trends = Trend.objects.all()
    context = {
        'keywords': keywords,
        'trends': trends,
    }
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    trends = Trend.objects.all()

    keyword = []
    result = []

    for trend in trends:
        keyword.append(trend.name)
        result.append(trend.result)

    plt.clf()
    plt.bar(keyword, result, label='Trends')

    plt.title('Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')

    buffer = BytesIO()
    plt.rcParams['font.family'] = 'Malgun Gothic'   # 한글 깨짐 방지
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()
    trendlist = Trend.objects.values_list('name', flat=True)

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
        
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search = soup.select_one('.LHJvCe')
        search = str(search).replace(',', '')
        search = str(search).split('검색결과 약 ')
        search = search[1]
        search = str(search).split('개')
        search = search[0]
        
        if keyword.name not in trendlist:
            trend = Trend.objects.create(name=keyword.name, result=search, search_period='year')
        else:
            trend = Trend.objects.get(name=keyword.name, search_period='year')
            if trend:
                trend.result = search
                trend.save()
            else:
                trend = Trend.objects.create(name=keyword.name, result=search, search_period='year')

    trends = Trend.objects.filter(search_period='year')
    search_keyword = []
    search_result = []

    for trend in trends:
        search_keyword.append(trend.name)
        search_result.append(trend.result)

    plt.clf()
    plt.bar(search_keyword, search_result, label='Trends')

    plt.title('Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')

    buffer = BytesIO()
    plt.rcParams['font.family'] = 'Malgun Gothic'   # 한글 깨짐 방지
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'keywords': keywords,
        'trends': trends,
        'chart': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_advanced.html', context)