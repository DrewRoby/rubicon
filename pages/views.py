from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user != 'AnonymousUser':# and request.user.is_athenticated == True:

        return render(request, 'pages/index.html')
    else:
        return render(request, 'pages/login.html')