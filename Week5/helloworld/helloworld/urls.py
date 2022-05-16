from django.contrib import admin
from django.urls import path, re_path
import myapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='hello_world'),
    path('test/', myapp.views.test),
    path('lotto/', myapp.views.lotto),
    path('lotto/result/', myapp.views.result),
]
 
# http://127.0.0.1:8000/
