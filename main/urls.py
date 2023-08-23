from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.couple_diary, name='index'),
    path('couplediary/', views.couple_diary, name='couple_diary'),
    path('mydiary/', views.my_diary, name='my_diary'),
    path('writing/', views.writing, name='writing'),
]
