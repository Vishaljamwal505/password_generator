from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generators/a.html')
def password(request):
     pass1=''
     char1=list("zxcvbnmlkjhgfdsaqwertyiop")
     if request.GET.get('uppercase'):
         char1.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('special'):
         char1.extend(list('!@#$%^&*'))
     if request.GET.get('number'):
         char1.extend(list('1234567890'))

     length=int(request.GET.get('length'))
     for x in range(length):
         pass1+=random.choice(char1)
     return render(request,'generators/pass.html',{'password':pass1})