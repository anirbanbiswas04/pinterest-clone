from django.contrib import admin
from .models import Pin, Like


class LikeInline(admin.TabularInline):
    model = Like


class PinAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'tag_list', 'created_at']
    search_fields = ['tags', 'created_by']
    list_filter = ['tags']
    inlines = [LikeInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Pin, PinAdmin)
