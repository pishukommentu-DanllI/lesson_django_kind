from django.shortcuts import render
from .forms import *


list_stations = [{'title': 'Тест страница', 'Text': 'Основная цель статьи - рассказать просто, на примере, как можно использовать паттерн делегирования в Swift. Статья состоит из двух частей. Первая - удалим из проекта Storyboard и напишем кодом простой интерфейс. Вторая - разберем, как с помощью делегата передать данные на предыдущий контроллер. Выбираем проект (стрелка 1), вкладка General и в разделе Deployment Info выделяем и удаляем Main(стрелка 2)', 'href': 'one.jpg'}]


def index(request):
    if request.method == 'POST':
        form = One(request.POST)
        if form.is_valid():
            dict_page = {}
            dict_page['title'] = form.cleaned_data['Title']
            dict_page['Url'] = form.cleaned_data['Url']
            dict_page['Text'] = form.cleaned_data['TextArea']
            dict_page['CheckBox'] = form.cleaned_data['CheckBox']
            dict_page['Selection'] = form.cleaned_data['Selection']
            list_stations.append(dict_page)
    return render(request, 'app/index.html', {'pages': list_stations})


def form(request):
    form = One()
    return render(request, 'app/form.html', {'form': form})