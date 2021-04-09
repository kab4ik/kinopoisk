from django.urls import path
from . import views

app_name = 'kinopoisk'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(),
         name='movie_detail'),
    path('movies/', views.MovieListView.as_view(),
         name='movie_list'),
    path('bestmovies/', views.BestMovieListView.as_view(),
         name='best_movie_list'),
    path('directors/', views.DirectorListView.as_view(),
         name='director_list'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(),
         name='director_detail'),
    path('movie/comment/<int:pk>/', views.add_comment,
         name='add_comment'),
    path('search/', views.search, name='search'),
    path('config/', views.config, name='config'),
    path('add_new_movie/', views.add_new_movie,
         name='add_new_movie'),
    path('add_new_director/', views.add_new_director,
         name='add_new_director'),
]