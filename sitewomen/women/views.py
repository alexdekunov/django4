from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


# menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить статью", 'url_name': "add_page"},
        {'title': "Обратная связь", 'url_name': "contact"},
        {'title': "Авторизация", 'url_name': "login"},
]

data_db = [
    {'id': 1, 'title': 'Анжелина', 'content': '''Биография Анжелины биография биография биография биография биография
    биография биография биография биография биография биография биография ''', 'is_published': True},
    {'id': 1, 'title': 'Hopper', 'content': 'Биография Hopper', 'is_published': False},
    {'id': 1, 'title': 'Truman', 'content': 'Биография Truman', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},

]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    # return HttpResponse("Страница приложения women")


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

# def categories(request, cat_id):  # HttpRequest
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")
#
#
# def categories_by_slug(request, cat_slug):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")
#
#
# def archive(request, year):
#     if year > 2023:
#         # uri = reverse('cats', args=('sport', ))
#         # return HttpResponsePermanentRedirect(uri)
#         # return redirect('cats', 'music')
#         return redirect('home')
#         # return redirect(index)
#         # return redirect('/', permanent=True)  # 301
#         # return redirect('/')  # 302
#         # raise Http404()
#
#     return HttpResponse(f"Архив по годам<p>{year}</p>")


def addpage(request):
    return HttpResponse(f"Добавление статьи")


def contact(request):
    return HttpResponse(f"Обратная связь")


def login(request):
    return HttpResponse(f"Авторизация")


def page_not_found(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

