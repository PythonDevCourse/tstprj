from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout

def auth(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/auth")
        else:
            return HttpResponseBadRequest("Не правильный пароль или имя пользоватеоля!")
    elif request.method == "GET":
        return render(template_name="login.html", request=request)
    else:
        return HttpResponseBadRequest("Request method error!")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/auth")