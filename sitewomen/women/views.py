from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):  # HttpRequest
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()

    return HttpResponse(f"Архив по годам<p>{year}</p>")


def page_not_found(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

