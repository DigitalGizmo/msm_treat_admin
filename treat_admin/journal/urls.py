from django.urls import path

from . import views

urlpatterns = [
    path('entries/', views.ListEntriesView.as_view(), name="entries"),
    path('plain_entries/', views.plain_entries, name='plain_entries'),
    path('test/', views.test, name='test'),
]
