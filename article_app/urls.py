from django.urls import path
from . import views
from .views import article_list_by_parameter, article_info, search_form, article_list_per_author

urlpatterns = [
    path('', views.home, name='home'),

    path('articles/<str:parameter>', article_list_by_parameter, name='articles_by_parameter'),
    path('article/info/<int:id>', article_info, name='article_info'),
    path('articles_per_author/<str:cur_id>', article_list_per_author, name='article_list_per_author'),
    path('search/', views.search_form, name='search_form'),
]
