from django.core.management import BaseCommand
from catalog.models import Product, Category
import json, psycopg2, os


class Command(BaseCommand):
    """
    Команда полного очищения БД и последующей загрузки данных из json файлов в папке data
    """

    def handle(self, *args, **options):

        # удаляем все данные из базы данных
        for something in (Product, Category):
            something.objects.all().delete()

        # загружаем данные по категориям из data_category.json из папки data
        with open('data/data_category.json', 'r', encoding='utf-8') as file:
            category = json.loads(file.read())
            with psycopg2.connect(host='localhost', database='catalog', user='postgres',
                                  password=os.environ['postgres']) as conn:
                with conn.cursor() as cur:
                    for i in range(0, len(category)):
                        cur.execute("INSERT INTO catalog_category VALUES (%s, %s, %s)",
                                    (category[i]['pk'],
                                     category[i]['fields']['name'],
                                     category[i]['fields']['description']))

        # загружаем данные по товарам из data_product.json из папки data
        with open('data/data_product.json', 'r', encoding='utf-8') as file:
            product = json.loads(file.read())
            with psycopg2.connect(host='localhost', database='catalog', user='postgres',
                                  password=os.environ['postgres']) as conn:
                with conn.cursor() as cur:
                    for i in range(0, len(product)):
                        cur.execute("INSERT INTO catalog_product VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                    (product[i]['pk'],
                                     product[i]['fields']['name'],
                                     product[i]['fields']['description'],
                                     product[i]['fields']['image'],
                                     product[i]['fields']['price'],
                                     product[i]['fields']['create_date'],
                                     product[i]['fields']['last_change_date'],
                                     product[i]['fields']['category']))





