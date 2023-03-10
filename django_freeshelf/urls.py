"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from books import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.list_books, name='home'),
    path("book/new", views.add_book, name="add_book"),
    path('book/<int:pk>', views.detail_book, name='detail_book'),
    path('book/<int:pk>/edit', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete', views.delete_book, name='delete_book'),
    path("private_place/", views.private_place, name='private'),
    path("accounts/", include("registration.backends.simple.urls")),
    path("staff_place/", views.staff_place, name='staff'),
    path('category/<slug:slug>', views.resource_category, name='category'),
    path('book/favorite/<int:pk>', views.favorite_book, name='favorite'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
