from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {
                "name": "Кофе",
                "description": "напиток из жареных и перемолотых зёрен кофейного дерева или кофейного куста.",
                "category": "Напитки",
                "price": 150,
                "date_of_creation": "2022-05-10 11:00",
                "date_of_change": "2022-05-10 11:10"
             },
            {
                "name": "Сыр",
                "description": "Пищевой продукт в виде твёрдой или полутвёрдой массы, получаемый в процессе сыроделия "
                               "из заквашиваемого особым способом молока.",
                "category": "Молочные продукты",
                "price": 200,
                "date_of_creation": "2022-05-10 19:00",
                "date_of_change": "2022-05-10 19:40"
            },
        ]

        products_objects = []
        for item in products_list:
            products_objects.append(Product(**item))

        Product.objects.bulk_create(products_objects)
