from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Reviews Admin Definition """

    list_display = (
        'created',
        '__str__',
        'room',
        'rating_average',
    )
