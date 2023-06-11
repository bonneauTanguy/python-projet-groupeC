"""
URL configuration for projet_groupe_c project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import (
    create_item,
    item_list,
    edit_item,
    delete_item,
    login_view,
    registration_view,
    index,
    get_password,
)

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("register/", registration_view, name="register"),
    path("login/", login_view, name="login"),
    path("create_item/", create_item, name="create_item"),
    path("item_list/", item_list, name="item_list"),
    path("/items/<int:item_id>/edit/", edit_item, name="edit_item"),
    path("item/<int:item_id>/delete/", delete_item, name="delete_item"),
    path("item/<int:item_id>/", get_password, name="get_password"),
]
