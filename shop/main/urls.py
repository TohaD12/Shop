from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path('signin', views.signin),
    path('signup', views.signup),
    path('pc', views.pc),
    path('phone', views.phone),
    path('accessories', views.accessories),
]
