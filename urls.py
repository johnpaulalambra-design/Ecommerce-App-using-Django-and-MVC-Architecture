
from django.contrib import admin
from django.urls import path, include
from main.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('inventory/', include('inventory.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('users/', include('users.urls')),
]
