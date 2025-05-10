
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1><a href='/about/'>About</a> | <a href='/contact/'>Contact</a>")

def about(request):
    return HttpResponse("<h1>About Page</h1><a href='/'>Home</a> | <a href='/contact/'>Contact</a>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1><a href='/'>Home</a> | <a href='/about/'>About</a>")
