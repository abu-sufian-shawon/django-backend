from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):
    
    def get(self, req):
        return render(template_name="login.html", request=req, context={})
    
    def post(self, request, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request = request, email = email, password = password)
        print(email)
        print(password)
        print(user)
        if user is not None:
            login(request=request, user=user)
            return HttpResponseRedirect(reverse('home'))

        else:
            return HttpResponse("Incorrect Credentials")

class SignUp(View):
    def get(self, req):
        return render(template_name="sign_up.html", request=req, context={})
    
    def post(self, request):
        data = request.POST
        full_name = data['full_name']
        email = data['email']
        phone = data['phone']
        password = data['password']

        CustomUser = get_user_model()
        user = CustomUser.objects.create_user (
            email = email,
            password = make_password(password),
        )

        user.backends = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponse("User created successfully")
    


class HomeView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        user = request.user
        if user is not None:
            print(user)
        return HttpResponse("Welcome to home page")