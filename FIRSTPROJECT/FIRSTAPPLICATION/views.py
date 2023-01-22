from django.shortcuts import render
from django.db import models
from .data import populate_data
from .models import *
from django.core import serializers

from django.http import JsonResponse

def my_view(request):
    populate_data()
    return 

def add_data(request):
    response = populate_data()
    return render(request, 'FIRSTAPPLICATION/home.html',{"data":response})

def home(request):
    # names= serializers.serialize('json', Name.objects.all())
    # ids= serializers.serialize('json', ID.objects.all())
    # contacts= serializers.serialize('json', Contact.objects.all())
    # addresses= serializers.serialize('json', Address.objects.all())
    # data = {'names':names,'ids':ids,'contacts':contacts,'addresses':addresses}
    # return render(request, 'FIRSTAPPLICATION/home.html',{'data':data})
    names = Name.objects.all()
    ids = ID.objects.all()
    contacts = Contact.objects.all()
    addresses = Address.objects.all()
    data = list(zip(names, ids, contacts, addresses))
    return render(request, 'FIRSTAPPLICATION/home.html',{'data':data})


# def home(request):
#     # populate_data()
#     name = Name.objects.all()
#     data = serializers.serialize(name)
#     return render(data, 'FIRSTAPPLICATION/home.html')
