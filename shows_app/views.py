from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from shows_app.models import Show, Band, City
from .forms import ShowForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from shows_app.serializers import ShowSerializer


def home_app(request):
    return render(request, 'home.html')


def home_show(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {'shows': shows})


@login_required(login_url='/admin/')
def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    form = ShowForm(instance=show)
    return render(request, 'shows/edit.html', {'form': form, 'show': show})


@login_required(login_url='/admin/')
def add_show(request):
    form = ShowForm()
    return render(request, 'shows/add.html', {'form': form})


@login_required(login_url='/admin/')
def save_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()

        shows = Show.objects.all()

        return render(request, 'shows/index.html', {'form': form, 'shows': shows})


@login_required(login_url='/admin/')
def update_show(request, show_id):
    if request.method == 'POST':
        show = Show.objects.get(id=show_id)
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()

        return redirect(home_show)


@login_required(login_url='/admin/')
def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect(home_show)


class ApiShowsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


# Create your views here.
def home_band(request):
    bands = Band.objects.all()
    return render(request, 'band/index.html', {'bands': bands})


@login_required(login_url='/admin/')
def edit_band(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'band/edit.html', {'band': band})


@login_required(login_url='/admin/')
def update_band(request, band_id):
    if request.method == 'POST':
        band = Band.objects.get(id=band_id)

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
def delete_band(request, band_id):
    band = Band.objects.get(id=band_id)
    band.delete()

    return redirect(home_band)


# Create your views here.
def home_city(request):
    city = City.objects.all()
    return render(request, 'city/index.html', {'city': city})


@login_required(login_url='/admin/')
def edit_city(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'city/edit.html', {'city': city})


@login_required(login_url='/admin/')
def update_city(request, city_id):
    if request.method == 'POST':
        city = City.objects.get(id=city_id)

        city.name = request.POST.get('name')
        city.state = request.POST.get('state')

        city.save()

        return redirect(home_city)


@login_required(login_url='/admin/')
def add_city(request):
    return render(request, 'city/add.html')


@login_required(login_url='/admin/')
def save_city(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state = request.POST.get('state')

        City.objects.create(
            name=name,
            state=state,
        )
        cities = City.objects.all()

        return render(request, 'city/index.html', {'city': cities})


@login_required(login_url='/admin/')
def delete_city(request, city_id):
    city = City.objects.get(id=city_id)
    city.delete()

    return redirect(home_city)
