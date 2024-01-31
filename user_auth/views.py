from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, get_user_model
from django.contrib.auth.hashers import make_password
import json

class LoginView(View):
    
    def get(self, req):
        return render(template_name="login.html", request=req, context={})
    
    def post(self, request, **kwargs):
        data = request.POST
        response = json.dumps(data)
        return HttpResponse(response, content_type="application/json")

class SignUp(View):
    def get(self, req):
        return render(template_name="sign_up.html", request=req, context={})
    
    def post(self, request):
        data = request.POST
        full_name = data['full_name']
        email = data['email']
        phone = data['phone']
        password = data['password']

        User = get_user_model()
        user = User.objects.create_user(
            full_name=full_name,
            email = email,
            phone = phone,
            password = make_password(password),
        )

        user.backends = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponse("User created successfully")