from django.shortcuts import   render , redirect
from django.contrib.auth import authenticate, login  
from django.contrib import messages

# Create your views here.
from .form import RegisterForm

def index(request):
    return render(request , 'accounts/index.html', {})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            form = RegisterForm()
    return render(request , 'accounts/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password :
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request , 'username or password is incorrect')
        else:
             messages.error(request, 'fillout all the fields')
    return render ( request, 'accounts/login.html',{})   
def home(request):
    return render(request, 'accounts/home.html', {}) 


