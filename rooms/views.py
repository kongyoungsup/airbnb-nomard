from pydoc import render_doc
from . import models
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

# (1) LIST - ListView 클래스로 구현


class HomeView(ListView):

    """HomeView Definitinon"""
    # Class-based views
    # https://ccbv.co.uk/projects/Django/2.2/

    model = models.Room  # template -> object_list
    context_object_name = 'pages'
    template_name = "rooms/home.html"
    page_kwarg = 'page'  # template -> page_obj (Paginator 상속)
    paginate_by = 10
    ordering = 'created'


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, 'rooms/detail.html', {'room': room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()  # > templates/404.html 를 보여준다.


# (2) LIST - python 코드로만 페이징 구현
''' 
from math import ceil  # python 반올림 함수
from pyexpat import model
from django.shortcuts import render
from . import models

# Function-based views
def all_rooms(request):

    # 페이징 구현 ,(url)../?page=1
    # .. ,1) = Defult //  or 1 = Defult
    page = int(request.GET.get("page", 1) or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    page_range = range(1, page_count + 1)
    print(page)
    print(page_count)

    return render(request, "rooms/home.html", context={
        "rooms": all_rooms,
        "page": page,
        "page_count": page_count,
        "page_range": page_range
    }
    )
'''

# (3) LIST - django - Paginator 페이징 구현
''' 
from . import models
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


def all_rooms(request):
    page = request.GET.get('page')
    room_list = models.Room.objects.all()
    # 5개 까지 남은 고아 페이지 를 앞 페이지와 합침
    paginator = Paginator(room_list, 10, orphans=5)

    try:  # request(?page=..)에러가 없을시에
        # get_page - request 값을 int 로 변경해주고 값이 없거나 다르면 1페이지로
        rooms = paginator.get_page(page)
        return render(request, "rooms/home.html", {
            "pages": rooms,
        })
    except:  # 에러가 있을 시에
        return redirect('/')
'''
