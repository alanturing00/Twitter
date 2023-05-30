from django.shortcuts import render,redirect, get_object_or_404
from .models import Profile,Twitt
from django.contrib import messages
from .forms import TwittForm,RegistrForm,Updateuserform,PicUser
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.http import HttpResponse
def home(request):
    if request.user.is_authenticated:
        form = TwittForm(request.POST or None)
        if request.method=="POST":
            if form.is_valid():
                twitts=form.save(commit=False)
                twitts.user=request.user
                twitts.save()
                messages.success(request,("your  tweet has been add succesfly"))
                return redirect('Twitt:home')

        twitt = Twitt.objects.all().order_by('-published')
        return render(request,'home.html',{"twitt":twitt,"form":form})
    else:
        # twitt = Twitt.objects.all().order_by('-published')
        # return render(request,'home.html',{"twitt":twitt})
        return HttpResponse('you muset og in first')

def like_twitt(request,pk):
    if request.user.is_authenticated:
        twitt = get_object_or_404(Twitt,id=pk)
        if twitt.like.filter(id=request.user.id):
            twitt.like.remove(request.user)
        else:
            twitt.like.add(request.user)
        return redirect('Twitt:home')
    else:
        return redirect('Twitt:logsin')

def individoual_twitt(request):
    if request.method=="POST":
        twitt = get_object_or_404(Twitt)
        return render(request,'individoual_twitt.html',{"twitt":twitt})
    else:
        return redirect('Twitt:home')
    


def profilelist(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request,'profilelist.html',{"profiles":profiles})
    else:
        messages.success(request,("you must be loged in to viwe this page..."))
        return redirect("Twitt:logsin")
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile= Profile.objects.get(user_id=pk)
        twitt = Twitt.objects.filter(user_id=pk).order_by('-published')

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST["follow"]
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action =='follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request,'profile.html',{"profile":profile,"twitt":twitt})
    else:
        messages.success(request,("you must be loged in to viwe this page..."))
        return redirect("Twitt:home")


def logsin(request):
    if request.method =='POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username, password= password)
        if user is not None:
            login(request,user)
            messages.success(request,('you loged in successfuly! '))
            return redirect('Twitt:home')
        elif user is None:
            messages.success(request,('username or password is wrong try again!'))
            return redirect('Twitt:logsin')
    else:        
        return render(request,'log.html',{})


def logsout(request):
    logout(request)
    return redirect('Twitt:logsin')


def registeruser(request):
    if request.user.is_authenticated:
        return redirect('Twitt:home')
    else:
        form = RegistrForm()
        if request.method =='POST':
            form = RegistrForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username= username, password= password)
                login(request,user)
                messages.success(request,('you have been add your account successfuly! Welcom!'))
                return redirect('Twitt:home')
        return render(request,'register.html',{'form':form})
    

def edit_user_info(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            user_form = Updateuserform(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('Twitt:home')
        else:
            user_form= Updateuserform(instance=request.user)
            return render(request,'edit_user_info.html',{'user_form':user_form})
    else:
        messages.success(request,('you must log in first!'))
        return redirect('Twitt:logsin')

def edit_pic(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            current_user=Profile.objects.get(user__id=request.user.id)

            profile_form= PicUser(request.POST or None, request.FILES or None, instance=current_user)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('Twitt:home')
        else:
            profile_form= PicUser(instance=request.user)
        return render(request,'edit_user_profile.html',{"profile_form":profile_form})


def changepassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('Twitt:home')
        else:
            form =PasswordChangeForm(user=request.user)
        return render(request,'passwordchange.html',{'form':form})
    else:
        messages.success(request,('you must have to log in first!'))
        return redirect('Twitt:logsin')
