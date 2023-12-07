from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from city.models import City


# Create your views here.
def home_city(request):
    city = City.objects.all()
    return render(request, 'city/index.html', {'city': city})


@login_required(login_url='/admin/')
def edit_city(request, id):
    city = City.objects.get(id=id)
    return render(request, 'city/edit.html', {'city': city})


@login_required(login_url='/admin/')
def update_city(request, id):
    if request.method == 'POST':
        city = City.objects.get(id=id)

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
def delete_city(request, id):
    city = City.objects.get(id=id)
    city.delete()

    return redirect(home_city)
