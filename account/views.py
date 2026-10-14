from typing import reveal_type

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import UserRegister, UserLogin



# Create your views here.


class UserRegisterView(View):
    form_class = UserRegister
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('book:home')
        return super().dispatch(request , *args, **kwargs)


    def get(self , request):
        form = self.form_class()
        return render(request , self.template_name , {'form':form})

    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            User.objects.create_user(cd['username'] , cd['email'] , cd['password1'])
            messages.success(request , 'User Created Successfully ! ' , 'success')
            return redirect('book:home')
        return render(request , self.template_name , {'form':form})



class UserLoginView(View):
    form_class = UserLogin
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('book:home')
        return super().dispatch(request , *args, **kwargs)

    def get(self , request):
        form =self.form_class
        return render(request , self.template_name , {'form':form})

    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            user =authenticate(request , username = cd['username'] , password = cd['password'])
            if user is not None:
                login(request , user)
                messages.success(request , 'You Logged in successfully ! ' , 'success')
                return redirect('book:home')
            messages.error(request , 'Invalid username or Invalid password ! ' , 'warning')
            return render(request , self.template_name , {'form':form})


class UserLogOutView(LoginRequiredMixin , View):
    login_url ='/account/login'

    def get(self , request):
        logout(request)
        messages.success(request , 'You logged out successfully ! ' , 'success')
        return redirect('book:home')
















