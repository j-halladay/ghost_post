"""ghost_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from ghost_post.views import homepage, addmessage, boasts, roasts, likes, unlike, like
from ghost_post.models import Message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('boasts/all', boasts),
    path('likes/all', likes),
    path('roasts/all', roasts),
    path('addmessage/', addmessage),
    path('like/<int:id>', like),
    path('unlike/<int:id>', unlike),



]
