from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Entry
import json

def test(request):
    return HttpResponse("Hello, world. This is a test.")

def plain_entries(request):
    entry_list = Entry.objects.all()
    output = '<br/> '.join([q.title for q in entry_list])
    return HttpResponse(output)

def entries(request):
    entry_list = Entry.objects.all()

    # use values() to create "flat" dictionary (excluding sub-lists)
    entry_list_of_dicts = entry_list.values('slug', 'title', 'lat', 
        'lon')

    # entry_list_of_dicts is actually a ValuesQuerySet
    # so we need to turn it into an actual list
    # and then use json.dumps to create json from list

    entry_list_of_dicts = json.dumps(list(entry_list_of_dicts))

    # print(" -- JSON output: " + str(JsonResponse(entry_list_of_dicts, safe=False)))

    # need special return type - can't just return string
    # JsonResponse seems to accept valid string
    return JsonResponse(entry_list_of_dicts, safe=False)
