import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Person


def retrive_all(request):
    # p = Person.objects.all()
    # person_list = list(p.values())
    # print(person_list)
    # return HttpResponse(person_list)
    person_dict = Person.objects.all()
    person_list = list()
    for person in person_dict:
        p = {"name": person.name, "country": person.country}
        person_list.append(p)
    print(person_list)
    return HttpResponse(person_list)



