from django.contrib import admin
from . import models
from django.utils.html import mark_safe
# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    def user_by(self, obj):
        return obj.rooms.count()

    list_display = (
        "name",
        "user_by",
    )

    fieldsets = (
        ("Basic Info",
            {
                "fields": ("name",)
            }),
    )

# Inline 모델


# (or) class PhotoInline(admin.StackedInline):
class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Model Definition """

    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

    # Inline 모델
    inlines = (PhotoInline,)

    #  리스트 정렬
    ordering = ("name", "price")

    # 본문 내용 셋 정렬
    fieldsets = (
        ("Basic Info",
            {
                "fields": ("name", "description", "country", "city", "address", "price", "room_type",)
            }),
        ("Times",
            {
                "fields": ("check_in", "check_out", "instant_book",)
            }),
        ("Spaces",
            {
                "fields": ("guests", "beds", "bedrooms", "baths",)
            }),
        ("MoreAbouttheSpaces",
            {
                "classes": ('collapse',),  # 확장/축소
                "fields": ("amenities", "facilities", "house_rules")
            }),
        ("Last Detail",
            {
                "fields": ("host", )
            }),
    )

    # 테이블에 보여줄 내용
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "count_amenities",
        "count_photos",
        "rating_count",
        "total_rating"
    )

    # 필터 적용할 내용
    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "city",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    # 검색 창
    # search_fields = ("^name",)    #startswith
    # search_fields = ("=name",)    #iexact
    # search_fields = ("=name", host__username)    #ForeignKey 찾기
    search_fields = (
        "name",
        "host__username",
    )

    # ManyToManyField 일때 사용하는 필터
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # 검색 창 띄우기, 셀렉트 박스내용이 많을때..
    raw_id_fields = ("host",)

    # many to many 필드의 갯수 표현
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = (
        '__str__', 'get_thumbnail'
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="80px" src="{obj.file.url}"')

    get_thumbnail.short_description = "썸네일"
