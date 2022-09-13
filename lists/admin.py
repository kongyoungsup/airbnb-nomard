from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'user',
        'rooms_count',
    )

    search_fields = ('name',)

    filter_horizontal = ('rooms',)
