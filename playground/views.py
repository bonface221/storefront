from django.shortcuts import render

# Create your views here.

def say_hello(request):
    context = dict(name = 'Mosh')

    return render(request,'hello.html',context)
