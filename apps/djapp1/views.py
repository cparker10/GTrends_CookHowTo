from django.shortcuts import render, redirect, HttpResponse
from . models import *
from django.contrib import messages
from time import gmtime, strftime, localtime
import bcrypt

def homepage(request):
    return render(request, 'djapp1/base.html', {})
    
    # Create your views here.
