from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
# Create your views here.

def log(request):
    return render(request,'registration/login.html')

def reset(request):
    return render(request,'registration/password_reset_confirm.html')

def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for{username}')  
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'registration/signup.html', {'form': form})





# def custom_logout(request):
#     logout(request)  
#     return redirect('post_list')