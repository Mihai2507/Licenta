from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages



def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

@login_required
def profil(request):
    return render(request, 'profil.html')


def send_message(request):
    if request.method == "POST":
        nume = request.POST.get('nume')
        prenume = request.POST.get('prenume')
        telefon = request.POST.get('telefon')
        email = request.POST.get('email')
        mesaj = request.POST.get('mesaj')

        subject = f"Mesaj de la {nume} {prenume}"
        message = f"Mesaj: {mesaj}\n\nNumăr de telefon: {telefon}\nEmail: {email}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['mihaic02@yahoo.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "Mesajul a fost trimis cu succes!")
        except Exception as e:
            messages.error(request, "A apărut o problemă la trimiterea mesajului. Te rugăm să încerci din nou!")


        return redirect('/?scroll_to=video4')

    return render(request, 'home.html')
