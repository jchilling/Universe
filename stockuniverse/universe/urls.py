from django.urls import path
from . import views

urlpatterns = [
    path('universe/', views.universe_list, name='universe_list'),
    path('universe/<int:pk>/', views.universe_detail, name='universe_detail'),
    path('universe/new/', views.universe_new, name='universe_new'),
]
