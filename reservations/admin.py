from django.contrib import admin
from . import models


@admin.register(models.Reservetions)
class ReservetionAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        'room',
        'status',
        'check_in',
        'check_out',
        'geust',
        'in_progress',
        'is_finished'
    )

    fieldsets = (
        ('basis', {'fields': ['status',
                              'check_in',
                              'check_out',
                              'geust',
                              'room', ]}),
    )
