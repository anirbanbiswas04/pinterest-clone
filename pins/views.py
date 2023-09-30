from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pin, Like
from taggit.models import Tag
from core.models import Profile
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .decorators import verify_owner


@login_required
def upload_pin(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None)
        tags = request.POST.get('tags', None)
        if image and tags:
            tags = [x for x in tags.replace(',', ' ').split(' ') if x != '']
            pin = Pin.objects.create(created_by=request.user, image=image)
            for tag in tags:
                pin.tags.add(Tag.objects.get_or_create(name=tag.strip())[0])
            pin.save()
        
            return render(request, 'core/parts/pin_upload_response.html', {'pin': pin})


@verify_owner
@login_required
def edit_pin(request, pk):
    pin = get_object_or_404(Pin, pk=pk)
    template_name = 'pins/edit_pin.html'
    
    if request.htmx:
        template_name = 'pins/parts/edit_pin_content.html'

    if request.method == 'POST':
        image = request.FILES.get('image', None)
        tags = request.POST['tags']
        if image and tags:
            pin.image = image

            pin.tags.clear()

            for tag in [x for x in tags.replace(',', ' ').split(' ') if x != '']:
                pin.tags.add(Tag.objects.get_or_create(name=tag.strip())[0])
            pin.save()
            template_name = 'pins/parts/view_pin_content.html'

    return render(request, template_name, {'pin': pin})


@verify_owner
@login_required
def delete_pin(request, pk):
    pin = get_object_or_404(Pin, pk=pk)
    pin.delete()

    if request.htmx:
        pins = Pin.objects.all()[:12]
        return render(request, 'core/parts/home_content.html', {'pins': pins})
    
    return redirect('home')


def view_pin(request, pk):
    pin = Pin.objects.prefetch_related('tags').get(pk=pk)
    template_name = 'pins/view_pin.html'
    if request.htmx:
        template_name = 'pins/parts/view_pin_content.html'

    return render(request, template_name, {'pin': pin})

def view_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    template_name = 'pins/view_tag.html'
    pin_obj = Paginator(Pin.objects.filter(tags__slug=tag.slug).distinct(), 12)
    pins = pin_obj.get_page(1)
    if request.htmx:
        template_name = 'pins/parts/view_tag_content.html'
        page = request.GET.get('page', None)
        if page:
            pins = pin_obj.get_page(page)
            template_name = 'core/parts/pins_grid_container.html'

    return render(request, template_name, {'pins': pins, 'tag': tag})

def profile(request, username):
    template_name = 'pins/profile.html'
    user = get_user_model().objects.prefetch_related('pins').get(username=username)
    pins_obj = Paginator(user.pins.all(), 12)
    pins = pins_obj.get_page(1)
    
    if request.htmx:
        template_name = 'pins/parts/profile_content.html'
        page = request.GET.get('page', None)
        if page:
            pins = pins_obj.get_page(page)
            template_name = 'core/parts/pins_grid_container.html'

    return render(request, template_name, {'user': user, 'pins': pins})

@login_required
def bio_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', None)
        profile.save()

        if request.htmx:
            return render(request, 'pins/parts/bio.html')

    return render(request, 'pins/parts/bio_edit.html', {'bio': profile.bio})


def search_pin(request):
    query = request.GET.get('query', '')
    pins = None
    template_name = 'pins/search.html'
    if query:
        search_terms = [x for x in query.replace(',', ' ').split(' ') if x != '']
        pins_obj = Paginator(Pin.objects.filter(tags__name__in=search_terms).distinct(), 12)
        pins = pins_obj.get_page(1)

    if request.htmx:
        template_name = 'pins/parts/search_content.html'
        page = request.GET.get('page', None)
        if page:
            pins = pins_obj.get_page(page)
            template_name = 'core/parts/pins_grid_container.html'

    return render(request, template_name, {'query': query, 'pins': pins})

@login_required
def toggle_like(request, pk):
    
    if request.method == 'POST':
        pin = get_object_or_404(Pin, pk=pk)
        instance, created = Like.objects.get_or_create(pin=pin, like_by=request.user)
        if not created:
            instance.delete()

        return render(request, 'pins/parts/like.html', {'pin': pin})
    
@login_required
def liked_pins(request):
    template_name = 'pins/liked_pins.html'
    pins_obj = Paginator(Pin.objects.filter(likes__like_by=request.user), 12)
    pins = pins_obj.get_page(1)

    if request.htmx:
        template_name = 'pins/parts/liked_pins_content.html'
        page = request.GET.get('page', None)
        if page:
            pins = pins_obj.get_page(page)
            template_name = 'core/parts/pins_grid_container.html'

    return render(request, template_name, {'pins': pins})
        
    
    


