from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from system.settings import EMAIL_HOST_USER
from .form import RegisterForm
from django.core.mail import send_mail

def home(request):
    return render(request,'accounts/home.html')

subject = "Account Creation"
message = "<h1>Your account has been created</h1>"

# User Register
def register(request):
    Form = RegisterForm
    if request.method =='POST':
        Form=RegisterForm(request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request,'User has been registered.')
            req = request.POST.dict()
            recepient =  req.get("email")
            send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return render(request,'accounts/register.html',{'form':Form})

def accounts(request):
    Form= RegisterForm()
    if request.method == 'POST':
        Form = RegisterForm(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(Form['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'accounts/success.html', {'recepient': recepient})
    return render(request, 'accounts/index.html', {'form':Form})    


