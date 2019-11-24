from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .models import Entry
from .serializers import EntriesSerializer


def test(request):
    return HttpResponse("Hello, world. This is a test.")

def plain_entries(request):
    entry_list = Entry.objects.all()
    output = '<br/> '.join([q.title for q in entry_list])
    return HttpResponse(output)

class ListEntriesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Entry.objects.all()
    serializer_class = EntriesSerializer

