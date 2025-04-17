from django.urls import path
from . import views
from . import convert

urlpatterns = [
    path('', views.home, name='home'), # root URL -> 127.0.0.1:8000/ -> run a function called home in views
    path('info', views.info, name='info'), # 127.0.0.1:8000/info -> run a function called info in views
    path('index', views.index, name='index'), # 127.0.0.1:8000/index
    path('check', views.age_check, name='check'), # 127.0.0.1:8000/check
    path('fruits', views.fruit_list, name='fruits'), # 127.0.0.1:8000/fruits
    path('input', views.input_form, name='input'), # 127.0.0.1:8000/input
    path('result', views.result, name='result'), # 127.0.0.1:8000/result
    path('convert', convert.currency_converter, name='converter'),
    path('timer', views.timer_view, name='timer'),
]   