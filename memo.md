# pipenv 설치

- pip 는 전역으로 설치되서 쓰기 불편함

# 맥 터미널, 프로젝트 폴더로 이동 - $ pipenv --three

// 파이선 가상환경 설치

# vscode 프로젝트 폴더, 터미널에서 - $ pipenv shell

// 파이선 가상환경으로 접속
// pc재시작 , 터미널 종료시 다시 접속, django-admin확인

# $ pipenv install Django==2.2.5

// 장고 2.2.5 설치

# $ django-admin

// 장고 설치 확인

# git 저장소 업로드

- gitignore 설정 - gitignore python 검색
  https://github.com/nomadcoders/airbnb-clone/commit/99fbc37feec152ce345bfa40a431da7861974365

# $ django-admin startproject config

- 장고 설치
- 생성된 config 폴더의 이름을 Aconfig로 바꾼디
- 내부레 config 폴더와 manager.py 파일을 최상위 폻더로 이동한다.
- Aconfig 폴더는 삭제
- manager.py 파일의 파이선 버젼 확인 3.xx (pipenv 선택) (vscode 하단)

# $ Python pep - 파이선 문법권장사항

- Linter, Formatter 설치

# $ python manage.py runserver

- 장고서버 실행

- Error: That port is already in use.
- sudo lsof -t -i tcp:8000 | xargs kill -9 (8000서버죽이기)

# $ python manage.py migrate

# $ python manage.py createsuperuser

# $ django-admin startapp rooms

# $ django-admin startapp users

# $ django-admin startapp reviews

# $ django-admin startapp conversations

$ django-admin startapp lists
$ django-admin startapp reservations

- 어플리케이션 생성 (복수형, room X, rooms O)

# users/models.py // 사용자 모델 추가

<!-- from django.contrib.auth.models import AbstractUser
     ..
     class User(AbstractUser):
     .. -->

# config/settings.py // Application definition 수정

<!-- DJANGO_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    PROJECT_APPS = ["users.apps.UsersConfig"]

    INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS -->

# 기본 사용자 모델을 오버라이드

-> config/settings.py

<!-- ...
     AUTH_USER_MODEL = 'users.User' -->

                  // (앱이름).(모델이름)

AUTH_USER_MODEL 설정값을 제공함으로써 기본 사용자 모델을 오버라이드

# 파일 삭제

db.sqlite3 파일, 0001..0002..
**pycache** 폴더
migrations 폴더내에 마이그레이션 파일

# $ python manage.py makemigrations

# $ python manage.py migrate

# $ python manage.py createsuperuser

# $ pipenv install Pillow

- 파이선 이미지 라이브러리


# $ django-admin startapp core

- 공통으로 사용되는 모델생선


# $ pipenv install django-countries

- 국가 리스트 생성 라이브러리
- django-countries 를 settings.py 에 app을 등록
- https://pypi.org/project/django-countries/
<!-- from django_countries.fields import CountryField -->


# $ 모델 설정 순서

     Model 설정 -> Admin 설정 -> Setting.py, Project_apps 설정 -> makemigrations -> migrate


# DEBUG = True

프로덕션 환경에서 디버그를 켜고 실행하지 마십시오!



# 이미지 경로 설정

## /config/settings.py

...
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

MEDIA_URL = "/media/"


## /config/urls.py

from django.conf import settings # settings.py 파일 불러옴
from django.conf.urls.static import static # static 파일 불러옴

..

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Django manager로 실행할 명령어 만들기, 데이터 베이스 만들기
- django의 manager.py 파일을 통해서 서버도 실행하고 model과 DB도 매핑하는 명령어를 실행합니다.
- 이런 명령어를 만드는 방법을 간단하게 소개 합니다.
- app내에 model과 동일한 경로에 management/commands 폴더를 생성
- 생성된 각 폴더에 __init__.py파일을 생성
- commands의 폴더에 명령어의 이름이 되는 파일을 생성 ex) hello.py

 > python manager.py hello


# Django Seed, Faker를 활용한 데이터 만들기
https://velog.io/@kmnkit/Django-Seed-Faker%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%B4%9D%EC%A0%95%EB%A6%AC

https://github.com/Brobin/django-seed

  > pipenv install django-seed
  에러 날시에...
  > pipenv install django-seed==0.2.2 

- faker
https://faker.readthedocs.io/en/master/providers/baseprovider.html  

