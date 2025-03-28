from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'wishes/home.html')

def wish_response(request):
    return HttpResponse("🎉 Thank you for your wishes! God bless you! 🙏😊")