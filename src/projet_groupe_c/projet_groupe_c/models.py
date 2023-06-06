from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ItemHistory(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    modification_date = models.DateTimeField()


class SharedItem(models.Model):
    sharing_user_id = models.IntegerField()
    shared_with_user_id = models.IntegerField()
    share_date = models.DateTimeField()


class Archived(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, primary_key=True)
    history = models.ForeignKey("ItemHistory", on_delete=models.CASCADE)


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    shared_item = models.ForeignKey("SharedItem", on_delete=models.CASCADE)


class Shared(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, primary_key=True)
    shared_item = models.ForeignKey("SharedItem", on_delete=models.CASCADE)
