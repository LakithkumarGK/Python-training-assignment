from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # root URL -> 127.0.0.1:8000/ -> run a function called home in views
    path('info', views.info, name='info'), # 127.0.0.1:8000/info -> run a function called info in views
    path('index', views.index, name='index')
]