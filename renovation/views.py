from django.shortcuts import render, render_to_response
# from teammate.forms import UserForm, UserProfileForm, TopicForm
# from teammate.models import Game, Instance, Attributes,Comment
from django.db.models import Q

from django import forms
from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

import os
from django.core.context_processors import csrf
from renovation.models import Scene

# Create your views here.



def index(request):
	items = Scene.objects.all()
	return render(request, 'renovation/index.html',{'items':items})

def list(request):
	scene = Scene.objects.all()
	return render(request, 'renovation/portfolio_masonry.html',{'scene':scene})

def scene_info(request, scene_id):
	item = Scene.objects.get(pk=scene_id)
	return render(request, 'renovation/scene_info.html',{'item':item})