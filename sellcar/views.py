from django.shortcuts import render, redirect,  get_object_or_404
from .forms import CarForm
from . import views
from .models import Car
from django.contrib.auth.decorators import login_required

@login_required
def sell_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('car_detail', id=car.id)

    else:
        form = CarForm()

    return render(request, 'sellcar.html', {'form': form})



def car_detail(request, id):
    # Căutăm mașina pe baza ID-ului
    car = get_object_or_404(Car, pk=id)

    # Returnăm pagina de detaliu a mașinii
    return render(request, 'car_detail.html', {'car': car})
