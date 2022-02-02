import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from myapp.models import Person


# Create your views here.
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


def add(request):
    if request.method == "POST":
        person_dict = json.loads(request.body)
        name = person_dict.get('name')
        country = person_dict.get('country')
        q = Person(name=name, country=country)
        q.save()
        return HttpResponse("Added")
