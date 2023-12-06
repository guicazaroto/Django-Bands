from django.shortcuts import render, redirect
from shows.models import Show
from .forms import ShowForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from shows.serializers import ShowSerializer

def home_show(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', { 'shows': shows })

def edit_show(request, id):
    show = Show.objects.get(id=id)
    form = ShowForm(instance=show)
    return render(request, 'shows/edit.html', { 'form': form, 'show': show })

def add_show(request):
    form = ShowForm()
    return render(request, 'shows/add.html', {'form': form})

def save_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()

        shows = Show.objects.all()

        return render(request, 'shows/index.html', { 'form': form, 'shows': shows })
    
def update_show(request, id):
    if request.method == 'POST':
        show = Show.objects.get(id=id)
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()

        return redirect(home_show)

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    
    return redirect(home_show)

class ApiShowsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer