from django.db import models
from django.utils.text import slugify
import random
import string

NULLABLE = {'blank': True, 'null': True}


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='URL')
    text = models.CharField(max_length=2000, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации')
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'Запись {self.title} от {self.create_date} c количеством просмотров {self.count_view}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-create_date',)

    def increase_views_count(self):
        self.count_view += 1
        self.save()



