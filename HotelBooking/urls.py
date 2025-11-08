"""HotelBooking URL Configuration

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
from django.urls import path,include
from . import settings
from HotelApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),

    path('',views.index,name='index'),
    path('profile/', views.profile, name='profile'),

    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



