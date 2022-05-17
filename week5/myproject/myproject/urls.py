from django.contrib import admin
from django.urls import path
import lotto.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/',lotto.views.home),
    path('lotto/result',lotto.views.result)
]
