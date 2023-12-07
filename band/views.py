from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from band.models import Band


# Create your views here.
def home_band(request):
    bands = Band.objects.all()
    return render(request, 'band/index.html', {'bands': bands})


@login_required(login_url='/admin/')
def edit_band(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'band/edit.html', {'band': band})


@login_required(login_url='/admin/')
def update_band(request, id):
    if request.method == 'POST':
        band = Band.objects.get(id=id)

        band.name = request.POST.get('name')
        band.genre = request.POST.get('genre')

        band.save()

        return redirect(home_band)


@login_required(login_url='/admin/')
def add_band(request):
    return render(request, 'band/add.html')


@login_required(login_url='/admin/')
def save_band(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre = request.POST.get('genre')

        Band.objects.create(
            name=name,
            genre=genre,
        )
        bands = Band.objects.all()

        return render(request, 'band/index.html', {'bands': bands})


@login_required(login_url='/admin/')
def delete_band(request, id):
    band = Band.objects.get(id=id)
    band.delete()

    return redirect(home_band)
