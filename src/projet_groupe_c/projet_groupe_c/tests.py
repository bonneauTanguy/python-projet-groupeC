from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, ItemHistory, SharedItem, Archived, Share, Shared


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.item = Item.objects.create(
            username="username",
            password="password",
            url="https://example.com",
            creation_date="2023-06-11T10:00:00Z",
            user=self.user,
        )
        self.item_history = ItemHistory.objects.create(
            username="username",
            password="password",
            url="https://example.com",
            modification_date="2023-06-11T11:00:00Z",
        )
        self.shared_item = SharedItem.objects.create(
            sharing_user_id=1, shared_with_user_id=2, share_date="2023-06-11T12:00:00Z"
        )
        self.archived = Archived.objects.create(
            item=self.item, history=self.item_history
        )
        self.share = Share.objects.create(user=self.user, shared_item=self.shared_item)
        self.shared = Shared.objects.create(
            item=self.item, shared_item=self.shared_item
        )

    def test_item_creation(self):
        self.assertEqual(self.item.username, "username")
        self.assertEqual(self.item.password, "password")
        self.assertEqual(self.item.url, "https://example.com")
        self.assertEqual(str(self.item.creation_date), "2023-06-11 10:00:00+00:00")
        self.assertEqual(self.item.user, self.user)

    def test_item_history_creation(self):
        self.assertEqual(self.item_history.username, "username")
        self.assertEqual(self.item_history.password, "password")
        self.assertEqual(self.item_history.url, "https://example.com")
        self.assertEqual(
            str(self.item_history.modification_date), "2023-06-11 11:00:00+00:00"
        )

    def test_shared_item_creation(self):
        self.assertEqual(self.shared_item.sharing_user_id, 1)
        self.assertEqual(self.shared_item.shared_with_user_id, 2)
        self.assertEqual(str(self.shared_item.share_date), "2023-06-11 12:00:00+00:00")

    def test_archived_creation(self):
        self.assertEqual(self.archived.item, self.item)
        self.assertEqual(self.archived.history, self.item_history)

    def test_share_creation(self):
        self.assertEqual(self.share.user, self.user)
        self.assertEqual(self.share.shared_item, self.shared_item)

    def test_shared_creation(self):
        self.assertEqual(self.shared.item, self.item)
        self.assertEqual(self.shared.shared_item, self.shared_item)
