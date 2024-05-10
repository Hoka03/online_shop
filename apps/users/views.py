from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import random
from django.contrib import messages
from datetime import timedelta
from django.utils.timezone import now

from apps.users.models import CustomUser, UserAuthCode
from apps.users.services import send_email_to_user


def register(request):
    return render(request, 'register_login/register.html')


def send_code_to_email(request):
    if request.method != 'POST':
        return redirect('register-page')

    email = request.POST.get('email')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')

    if not email:
        messages.error(request, 'Email was not entered')
        return redirect('register-page')

    if not password or not re_password:
        messages.error(request, 'Password or re_password was not entered')
        return redirect('register-page')

    if password != re_password:
        messages.error(request, 'All passwords was not entered')
        return redirect('register-page')

    if CustomUser.objects.filter(email=email).last():
        messages.error(request, 'This email was login before, Please choose other email!!!')
        return redirect('register-page')

    code = random.randint(1000, 10000)
    send_email_to_user(email, code)
    UserAuthCode.objects.create(email=email, code=code, expire_at=now()+timedelta(minutes=5))

    context = {
        'email': email,
        'password': password,
        'code': '',
        'code_error': '',
    }

    return render(request, 'register_login/confirm_email.html', context)


def register_user(request):
    if request.method != 'POST':
        return redirect('register-page')

    email = request.POST.get('email')
    password = request.POST.get('password')
    code = request.POST.get('code')

    UserAuthCode.objects.filter(expire_at__lte=now()).delete()

    obj = UserAuthCode.objects.filter(email=email, code=code, expire_at__gte=now())

    if obj.last():
        CustomUser.objects.create_user(email=email, password=password)
        obj.delete()
    elif UserAuthCode.objects.filter(email=email, expire_at__gte=now()):
        context = {
            'email': email,
            'password': password,
            'code': code,
            'code_error': 'Code not valid.',
        }
        return render(request, 'register_login/confirm_email.html', context)
    else:
        messages.error(request, 'Email or Password was entered mistake')
        return redirect('register-page')

    return render(request, 'register_login/login.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            messages.error(request, 'Email was not entered')
            return redirect('login-page')

        if not password:
            messages.error(request, 'password was not entered')
            return redirect('login-page')

        user = authenticate(request=request, email=email, password=password)

        if not user:
            messages.error(request, 'Login or name was entered mistake')
            return redirect('login-page')

        login(request, user)
        return redirect('home-page')

    return render(request, 'register_login/login.html')


def log_out(request):
    logout(request)
    return redirect('home-page')
