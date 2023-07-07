from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

#def index1(response):
#    return HttpResponse('tech with tim')

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    itemsFromList = ls.item_set.get(id=1)
    
    return HttpResponse('<h1> %s </h1>' % (ls.name, itemsFromList.name))
   
    