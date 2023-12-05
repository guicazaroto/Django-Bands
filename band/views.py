from django.shortcuts import render
from band.models import Band

# Create your views here.
def home_band(request):
    bands = Band.objects.all()
    return render(request, 'band/index.html', { 'bands': bands })
