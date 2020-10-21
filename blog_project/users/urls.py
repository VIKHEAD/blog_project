from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('name/<str:first_name>/', views.name, name='name'),
    path('surname/<str:last_name>/', views.surname, name='surname'),
    path('age/<int:user_age>/', views.age, name='age')
]