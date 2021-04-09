from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    context = {
        'last_movies': sorted(Movie.objects.all(),
                              key=lambda x: -x.id)[:4],
        'best_movies': Movie.objects.order_by('-rating')[:4],
        'directors': Director.objects.order_by('-id')[:4],
    }
    return render(request,
                  'kinopoisk/index.html',
                  context)

class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = CommentForm()
        return context

class MovieListView(ListView):
    model = Movie

class BestMovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(rating__gte=8.0).order_by('-rating')
    template_name = 'kinopoisk/best_movie_list.html'

class DirectorListView(ListView):
    model = Director

class DirectorDetailView(DetailView):
    model = Director

def add_comment(request, pk):
    try:
        text = request.POST.get('text')
        author = request.POST.get('author')
        if text and author:
            comment = Comment(text=text,
                              author=author,
                              movie=Movie.objects.get(pk=pk))
            comment.save()
    except:
        print('не смогли добавить комментарий')
    finally:
        return HttpResponseRedirect(reverse('kinopoisk:movie_detail',
                                            args=(pk,)))

def search(request):
    search = request.POST.get('search')
    if search:
        #movies = Movie.objects.filter(title__icontains=search)
        movies = [movie for movie in Movie.objects.all() if search.lower() in movie.title.lower()]
        directors = [director for director in Director.objects.all() if search.lower()
                     in director.last.lower() or search.lower() in director.first.lower()]
        context = {
            'search': search,
            'movies': movies,
            'directors': directors,
        }
        return render(request, 'kinopoisk/search.html', context)
    else:
        return redirect(reverse('kinopoisk:index'))


def config(request):
    context = {
        'movie_model_form': MovieModelForm(),
        'director_model_form': DirectorModelForm(),
    }
    return render(request, 'kinopoisk/config.html', context)

def add_new_movie(request):
    form = MovieModelForm(request.POST)
    saved = form.save(commit=False)
    saved.poster = request.FILES['poster']
    saved.save()
    return HttpResponseRedirect(reverse('kinopoisk:index'))

def add_new_director(request):
    form = DirectorModelForm(request.POST)
    saved = form.save(commit=False)
    saved.portait = request.FILES['portrait']
    saved.save()
    return HttpResponseRedirect(reverse('kinopoisk:index'))