from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def categories(request, cat_id):
    if cat_id > 1000:
        raise Http404()
    return HttpResponse(f"<h1>Статьи по категориям: </h1> <p>id = {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям: </h1> <p>slug = {cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def index(request):
    context = {'title': 'главная страница сайта', 'menu': menu}
    return render(request, 'woman/index.html', context=context)


def about(request):
    context = {'title': 'О сайте'}
    return render(request, 'woman/about.html', context)