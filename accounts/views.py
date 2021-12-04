from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,'accounts/home.html')


# User Register
def register(request):
    Form = UserCreationForm
    if request.method =='POST':
        Form=UserCreationForm(request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request,'User has been registered.')
    return render(request,'accounts/register.html',{'form':Form})


