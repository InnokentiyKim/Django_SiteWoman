from django.urls import path

from . import views


urlpatterns = [
    path('cats/<int:cat_id>/', views.categories, name='categories'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='categories_slug'),
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
]

handler404 = views.page_not_found