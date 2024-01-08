from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_lenght=100, unique=True, verbose_name='URL')
    text = models.CharField(max_length=2000, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение')
    create_date = models.DateTimeField(verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации')
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'Запись {self.title} от {self.create_date} c количеством просмотров {self.count_view}'





