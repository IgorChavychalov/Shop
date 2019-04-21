from django.core.management.base import BaseCommand
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        # обращения к модели (имя класса) обязательно в нижнем регистре
        users = ShopUser.objects.filter(shopuserprofile__isnull=True)
        for user in users:
            ShopUserProfile.objects.create(user=user)
