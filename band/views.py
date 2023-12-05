from django.shortcuts import render, redirect
from band.models import Band

# Create your views here.
def home_band(request):
    bands = Band.objects.all()
    return render(request, 'band/index.html', { 'bands': bands })

def edit_band(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'band/edit.html', { 'band': band })

def update_band(request, id):
    if request.method == 'POST':
        band = Band.objects.get(id=id)

        band.name = request.POST.get('name')
        band.genre = request.POST.get('genre')

        band.save()

        return redirect(home_band)
