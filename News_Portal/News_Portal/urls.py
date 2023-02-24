"""News_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from News_Portal_app.views import IndexView
from django.contrib.auth.views import LogoutView
from News_Portal_app.views import upgrade_me

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('News_Portal_app.urls')),
   path('articles/', include('News_Portal_app.urls_article')),
   path('accounts/', include('allauth.urls')),
   path('', IndexView.as_view()),
   path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
   path('upgrade/', upgrade_me, name = 'upgrade')
]
