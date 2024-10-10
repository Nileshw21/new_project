from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'index.html')



def dynamic_path(request, num):
    print(num)
    return HttpResponse("This is dynamic path page")