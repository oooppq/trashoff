from django.shortcuts import render, redirect
from django.contrib import auth
# from django.contrib.auth.models import User
from accounts.models import User

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        id = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username=id, password=pw)
        if user != None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        again = request.POST['again']
        if password != again: return render(request, 'register.html')
        email = request.POST['email']
        nickname = request.POST['nickname']
        university = request.POST['university']
        photo = request.FILES['photo']
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        nickname=nickname,
                                        photo=photo,
                                        university=university,
                                        )
        return redirect('home')
    
def myPage(request):
    return render(request, 'my-page.html')

def profileModify(request):
    if request.method == "GET":
        return render(request, 'profile-modify.html')
    elif request.method == "POST":
        user = request.user
        
        if request.POST['password'] != '':  
            if request.POST['password'] == request.POST['again']:
                user.password = request.POST['password']
        user.email = request.POST['email']
        user.nickname = request.POST['nickname']
        if request.POST['university'] != 'none':
            user.university = request.POST['university']
        user.comments = request.POST['comments']
        user.save()
        return redirect('mypage')

def congrats(request):
    return render(request, 'congrats.html')