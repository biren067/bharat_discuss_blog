from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .UserRegistrationFrom import UserRegistrationFrom

def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("Successfull working ",username)
            messages.success(request,f"{username} is created successfully.")
            return redirect("blog-home")
    else:
        form =  UserRegistrationFrom()
    return render(request,template_name='users/register.html',context={'form':form})