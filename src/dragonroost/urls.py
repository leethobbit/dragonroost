"""
URL configuration for Dragonroost project.

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
from django.contrib.auth.models import User
from django.urls import include, path

from .views import HomeListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeListView.as_view(), name="home_list"),
    path("accounts/", include("apps.accounts.urls")),
    path("animals/", include("apps.animals.urls", namespace="animals")),
    path("business/", include("apps.business.urls", namespace="business")),
    path("medical/", include("apps.medical.urls", namespace="medical")),
    path("people/", include("apps.people.urls", namespace="people")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
