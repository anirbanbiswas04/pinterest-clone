from django.urls import path
from .views import (
        upload_pin, view_pin, 
        search_pin, edit_pin, 
        delete_pin, view_tag, 
        profile, bio_edit,
        toggle_like, liked_pins
    )

app_name = 'pins'

urlpatterns = [
    path('upload-pin/', upload_pin, name='upload_pin'),
    path('search-pin/', search_pin, name='search_pin'),
    path('bio-edit/', bio_edit, name='bio_edit'),
    path('liked-pins/', liked_pins, name='liked_pins'),
    path('view-pin/<int:pk>/', view_pin, name='view_pin'),
    path('edit-pin/<int:pk>/', edit_pin, name='edit_pin'),
    path('toggle-like/<int:pk>/', toggle_like, name='toggle_like'),
    path('delete-pin/<int:pk>/', delete_pin, name='delete_pin'),
    path('view-tag/<slug:slug>/', view_tag, name='view_tag'),
    path('profile/<str:username>', profile, name='profile'),
]
