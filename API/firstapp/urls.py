"""backend URL Configuration

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
from django.urls import path
from .views import *

urlpatterns = [
    path("works/", WorksGetPost.as_view()),
    path("project/", ProjectView.as_view()),
    path("worktype/", WorkTypeView.as_view()),
    path("workstatus/", WorkStatusView.as_view()),
    path("workupdate/<int:id>",WorkUpdate.as_view()),
    path("workdelete/<int:id>",WorkDelete.as_view()),
    path("date/",GetCurrentDate.as_view())
]
