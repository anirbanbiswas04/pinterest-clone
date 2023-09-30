from .models import Pin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied


def verify_owner(function):
    def wrapper(request, *args, **kwargs):
        pin = get_object_or_404(Pin, pk=kwargs.get('pk'))
        if request.user != pin.created_by:
            raise PermissionDenied

        return function(request, *args, **kwargs)

    return wrapper
