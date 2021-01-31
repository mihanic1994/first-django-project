"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import tours.views as tours_views
from tours.views import my_handler404
from tours.views import my_handler500

handler500 = my_handler500
handler404 = my_handler404
urlpatterns = [
    path('', tours_views.main_view),
    path('departure/<str:departure>', tours_views.departure_view),
    path('tour/<int:ident>', tours_views.tour_view),
]
