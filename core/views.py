from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth import login
from pins.models import Pin


def home(request):
    template_name = 'core/home.html'
    pins_obj = Paginator(Pin.objects.all(), 12)
    pins = pins_obj.get_page(1)

    if request.htmx:
        template_name = 'core/parts/home_content.html'
        page = request.GET.get('page', None)
        if page:
            pins = pins_obj.get_page(page)
            template_name = 'core/parts/pins_grid_container.html'

    return render(request, template_name, {'pins': pins})


def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'core/signup.html', {'form': form})
