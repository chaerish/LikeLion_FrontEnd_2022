"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views #views.py를 myapp으로부터 가져옴 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/',views.lottoStart,name='lottostart'), #입력화면 연결 : /lotto를 치면 함수 이름은 lotto고, views안에 있는 lotto 함수로 갈거야 
    path('lotto/result',views.lotto,name='lotto'),
]
#http://127.0.0.1:8000/
#"path('',myapp.views.home,name="hello_world"), //''는 슬래쉬 뒤에 아무것도 없을 때 실행된다는것 
