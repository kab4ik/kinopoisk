from django.db import models
from django.urls import reverse
import datetime

class Director(models.Model):
    last = models.CharField('фамилия', max_length=20)
    first = models.CharField('имя', max_length=20)
    portrait = models.ImageField('портрет', null=True, blank=True, upload_to='directors/')

    def __str__(self):
        return f'{self.first} {self.last}'

    def get_absolute_url(self):
        return reverse('kinopoisk:director_detail',
                       args=(self.id,))

    def best_movie(self):
        if self.movie_set:
            return self.movie_set.order_by('-rating')[0]
        else:
            return None

    class Meta:
        ordering = ['last', 'first']


class Movie(models.Model):
    title = models.CharField('название', max_length=20)
    year = models.IntegerField('год выхода', null=True, blank=True)
    director = models.ForeignKey(Director, help_text='режиссер', on_delete=models.SET_NULL,
                                 blank=True, null=True)
    rating = models.FloatField('рейтинг', default=5.0)
    poster = models.ImageField('постер', null=True, blank=True, upload_to='posters/')
    plot = models.FileField('сюжет', null=True, blank=True, upload_to='plots/')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('kinopoisk:movie_detail',
                       args=(self.id,))
    class Meta:
        ordering = ['year']


class Comment(models.Model):
    movie = models.ForeignKey(Movie, help_text='фильм', on_delete=models.CASCADE)
    text = models.TextField('комментарий')
    author = models.CharField('автор', max_length=30)
    date_time = models.DateTimeField('дата и время', default=datetime.datetime.now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-date_time']