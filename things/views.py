from django.shortcuts import render
from .models import Thing
from .forms import ThingForm
def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
