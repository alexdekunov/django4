from django.urls import path, re_path, register_converter
from women import views
from women import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
    path("archive/<year4:year>/", views.archive, name='archive'),
]

