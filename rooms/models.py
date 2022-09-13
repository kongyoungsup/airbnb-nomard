from tabnanny import verbose
from venv import create
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from django.urls import reverse

# Create your models here.


class AbstractItem(core_models.TimeStampModel):

    """ Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    # 리스트 타이틀 설정
    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition """

    # verbose_name, 임의의 네이밍지정 + s
    class Meta:
        verbose_name = "Room Type"
        ordering = ['-created']  # 생성 날짜별 순서지정, -created (역순), -created (정방향)


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    # verbose_name_plural, 임의의 네이밍 지정
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        'Room', related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=140, null=True, blank=True)
    guests = models.IntegerField(null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    baths = models.IntegerField(null=True, blank=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    instant_book = models.BooleanField(default=False)

    # 하나의 연결이 필요하다면 *ForeignKey()
    # CASCADE(폭포수) #부모가 삭제 되면 같이 삭제
    # PROTECT(보호) #부모가 삭제 되도 삭제되지 않음
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, null=True, blank=True)
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True)

    # 여러개의 연결이 필요 하다면 *ManyToManyField()
    amenities = models.ManyToManyField(
        "Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField(
        "Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        "HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def rating_count(self):
        return self.reviews.count()

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        for var_reviews in all_reviews:
            all_rating += var_reviews.rating_average()

        if len(all_reviews) > 0:
            return all_rating / len(all_reviews)
        else:
            return 0

    # model 오버라이딩 ,데이터 앞글자를 대문자로 변경해서 저장
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    # detail View 로 이동 링크 만들기
    # from django.urls import reverse
    def get_absolute_url(self):
        return reverse('rooms:detail', kwargs={'pk': self.pk})
