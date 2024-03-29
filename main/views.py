from django.shortcuts import render,redirect
from .forms import SignUp,Register, UserForm
from .models import User
 


def index(recuest):
    users= User.objects.all()
    return render(recuest,'main/index.html',{'users':users})

def sign_up(request):
    form = SignUp()
    return render(request,'main/sign_up.html',{'form': form})

def registr(request):
    form = Register
    print(request.POST)   
    return render(request,"main/registr.html",{"register": form})

def add_user(request):
    form = UserForm()
    if request.method == "POST":
        form =UserForm(request.POST)
        if form.is_valid():
            User.objects.create(
                user_id=form.cleaned_data.get('user_id'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                about=form.cleaned_data.get('about'),
                is_married=form.cleaned_data.get('is_married'),
                birthday=form.cleaned_data.get('birthday')
            )
            return redirect('index')
            

    return render(request,"main/create_user.html", {'form':form} )


def update_user(request,pk):
    user =User.objects.get(id=pk)
    form =UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,"main/update_user.html",{"form": form})



def delete_user(request,pk):
    user =User.objects.get(id=pk)
    user.delete()
    return redirect('index')


