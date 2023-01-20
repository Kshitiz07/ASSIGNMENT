from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('FIRSTAPPLICATION/base.html')
    return HttpResponse(template.render())