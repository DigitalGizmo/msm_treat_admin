from django.urls import path

from . import views

urlpatterns = [
    path('entries', views.entries, name='entries'),
    path('plain_entries', views.plain_entries, name='plain_entries'),
    path('test', views.test, name='test'),
]
