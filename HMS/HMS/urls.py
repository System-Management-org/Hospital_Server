"""
URL configuration for HMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('conditions/', include('conditions.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('process/', include('hospital_processes.urls')),
    path('staff/', include('staff.urls')),
    path('inventory/', include('inventory.urls')),
    path('cashier/', include('cashier.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)