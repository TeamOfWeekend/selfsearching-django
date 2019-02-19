from django.contrib import admin

# Register your models here.
from films.models import Movie


admin.site.register(Movie)
