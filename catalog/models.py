from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')
    create_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_change_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, null=True,
                             verbose_name ='пользователь')
    is_published = models.BooleanField(default=False, verbose_name='опубликован?')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        permissions = [
            ('set_published', 'Can publish posts'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category')
        ]

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def has_permission_to_change(self, user):
        return self.user == user

    def has_permission_to_delete(self, user):
        return self.user == user


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version = models.IntegerField(verbose_name='номер версии')
    title_version = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='признак текущей версии', default=False, **NULLABLE)

    def __str__(self):
        return f'{self.title_version} ({self.product})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'