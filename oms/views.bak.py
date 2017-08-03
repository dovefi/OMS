from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Oms_user
from django.template import loader
import logging

def index(request):
    template = loader.get_template('oms/index.html')
    user_list = Oms_user.objects.all()
    content = {
        'user_list' : user_list,
    }
    print(user_list[0].user_name)
    return HttpResponse(template.render(content, request))
