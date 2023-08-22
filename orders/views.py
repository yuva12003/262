from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import data1


def index2(request):
    pro = data1.objects.all().values()
    output=" "
    for x in pro:
        output += x["product"]+x["price"]
    return HttpResponse(output)

def index3(request):
    pro = data1.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'pro': pro,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
