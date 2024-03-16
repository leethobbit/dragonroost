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
from django.urls import include, path
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, Site, ModelViewset, AppMenuMixin

from .views import HomeListView
from apps.animals.viewsets import AnimalViewSet, SpeciesViewSet
from apps.people.viewsets import PersonViewSet
from apps.business.viewsets import LocationViewSet

site = Site(
    title="Dragonroost",
    primary_color="#03989e",
    secondary_color="#015b5e",
    viewsets=[
        Application(
            title="Animals",
            icon="pets",
            app_name="animals",
            viewsets=[
                AnimalViewSet(),
                SpeciesViewSet(),
                ]
            ),
        Application(
            title="People",
            icon="group",
            app_name="people",
            viewsets=[
                PersonViewSet()
                ]
            ),
        Application(
            title="Business",
            icon="money",
            app_name="business",
            viewsets=[
                LocationViewSet()
            ]
        )
        ]
    )

urlpatterns = [
    path("", site.urls),
    path("admin/", admin.site.urls),
    path("", HomeListView.as_view(), name="home-list"),
    path("accounts/", include("apps.accounts.urls")),
    path("old/animals/", include("apps.animals.urls", namespace="old-animals")),
    path("old/business/", include("apps.business.urls", namespace="old-business")),
    path("old/medical/", include("apps.medical.urls", namespace="old-medical")),
    path("old/people/", include("apps.people.urls", namespace="old-people")),
    # path('hello/', hello_django, name='hello_django')
    # path("/", views.animal_list, name='animal_list')
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)