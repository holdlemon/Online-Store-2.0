from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление тестовых данных из фикстур"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загружаем данные из подготовленных фикстур
        call_command("loaddata", "category_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Категории из фикстур загружены успешно!"))
        call_command("loaddata", "product_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Продукты из фикстур загружены успешно!"))
