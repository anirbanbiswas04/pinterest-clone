from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
                path('', home, name='home'),
                path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
                path('logout/', LogoutView.as_view(), name='logout'),
                path('signup/', signup, name='signup'),
                path('pins/', include('pins.urls')),
                path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
