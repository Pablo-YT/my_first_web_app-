"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from my_first_web_app.my_first_web_app.views import root, home_page, portfolio_page, about_me,favourites
from django.urls import path



urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio_page),
    path('about.me/', about_me),
    path('favourites', favourites)
]

urlpatterns = [
    path('', root),
    path('home/', home_page)
]