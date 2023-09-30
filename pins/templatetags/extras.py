from django import template
from pins.models import Pin


register = template.Library()


@register.simple_tag
def is_liked(pin_id, user):
    if not Pin.objects.filter(id=pin_id, likes__like_by=user).exists():
        return 'is-outlined' 