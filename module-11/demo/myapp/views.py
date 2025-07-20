from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Jacoby says Hello!")