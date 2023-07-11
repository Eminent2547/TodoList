from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Task/<str:pk>/done', views.done, name='done'),
    path('Task/<str:pk>/delete', views.delete, name='delete'),
]