from django.contrib import admin
from .models import *

#admin.site.register(Director)
#admin.site.register(Movie)
#admin.site.register(Comment)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'rating')
    list_filter = ('year', 'director', )

class MovieInlines(admin.TabularInline):
    model = Movie
    extra = 1

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last', 'first',)
    list_filter = ( 'last', )
    inlines = [MovieInlines]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'date_time', 'movie',)
    list_filter = ( 'author', )
