from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Handles login, logout, etc.

    # Your app-specific URLs
    path('chipin/', include('chipin.urls')),  # Include your app's URLs here
]

