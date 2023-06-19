from django.shortcuts import render, redirect
from .models import Universe, Stock
from .forms import UniverseForm

def universe_list(request):
    universes = Universe.objects.all()
    return render(request, 'universe/universe_list.html', {'universes': universes})

def universe_detail(request, pk):
    universe = Universe.objects.get(id=pk)
    return render(request, 'universe/universe_detail.html', {'universe': universe})

def universe_new(request):
    if request.method == "POST":
        form = UniverseForm(request.POST)
        if form.is_valid():
            universe = form.save(commit=False)
            universe.user = request.user
            universe.save()
            return redirect('universe_detail', pk=universe.pk)
    else:
        form = UniverseForm()
    return render(request, 'universe/universe_edit.html', {'form': form})
