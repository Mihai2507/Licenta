from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()

            subject = "Activare cont"
            message = f"Salut, {user.username}! Apasa click pe link pentru a activa contul:\nhttp://localhost:8000/signup/activate/{user.id}/"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            messages.success(request, "Verifica-ti mail-ul pentru activare!")
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def activate(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, "Cont activat! Acum te poti autentifica!")
        return redirect('login')
    except User.DoesNotExist:
        messages.error(request, "Link invalid!")
        return redirect('signup')