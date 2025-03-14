from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profil(request):
    if request.method == 'POST':
        nume = request.POST.get('nume')
        prenume = request.POST.get('prenume')

        request.user.last_name = nume
        request.user.first_name = prenume
        request.user.save()
        messages.success(request, 'Datele tale au fost actualizate cu succes!')
        return redirect('profil')

    context = {
        'username': request.user.username,
        'nume': request.user.last_name,
        'prenume': request.user.first_name,
        'email': request.user.email,
    }
    return render(request, 'profil.html', context)
