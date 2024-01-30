from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('/auth/login')  # Redirect to your home page or any desired page
        else:
            return HttpResponse("Sign Up Failed")