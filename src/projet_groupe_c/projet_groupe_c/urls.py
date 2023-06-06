from django.contrib import admin
from django.urls import include, path
from .views import create_item, item_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create_item", create_item, name="create_item"),
    path("item_list", item_list, name="item_list"),
]
