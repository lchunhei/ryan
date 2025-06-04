from django.shortcuts import render, redirect          #django既lib，係virtualen拎
from django.contrib import messages, auth
from django.contrib.auth.models import User         #自己做user profile先可以多D data field, django only只有下面
# Create your views here.



def register(request):
    if request.method == 'POST':                #IF register html's form係用POST
        first_name = request.POST['first_name']     #右邊=from web輸入 -> 代入左邊!!!!!
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:               #如打相同
            if User.objects.filter(username=username).exists():     #check user已注冊?  左邊係model=database , 右邊係web form
                messages.error(request, 'Username already exists ! ')       #將句野入落messages ; error/sucess係用黎分顏色
                return redirect('accounts:register')                    #messages係_alert用
            else:
                if User.objects.filter(email=email).exists():     #check email已注冊?
                    messages.error(request, 'Email already exists ! ')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()         #create + save 資料
                    messages.success(request, 'Account created successfully !')
                    return redirect('accounts:register')
        else:
            messages.error(request, 'Passwords do not match !')
            return redirect('accounts:register')    #redirect=endpoint, use user cache, no need 重做page,快d
    else:
        return render (request, 'accounts/register.html')   #無token再行一次 ; 


def login(request):
    if request.method == 'POST':
        username = request.POST['username']      #form入黎
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request, user)           #login
            messages.success(request, 'You are now logged in ! ')
            return redirect('accounts:dashboard')           #如果成功去dashboard
        else:
            messages.error(request, 'Invalid credentials ! ')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect (request, 'accounts/logout.html')


def dashboard(request):
    return render (request, 'accounts/dashboard.html')








