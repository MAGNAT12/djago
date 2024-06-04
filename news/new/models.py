from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано ли')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,verbose_name='Категория', null=True) ## мы добавили новое поле. Здесь СУБД нас ограничивает созданием новой записи, и не позволит создать новое поле, потому что наше поле не заполнено как то, поэтому мы используем null=True. Поэтому желательно всегда сначала заранее продумать и построить модели, чтобы не сталкиваться с такими трудностями.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at',]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории') ## db_index делает поле более индексированным для базы данных

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    ordering = ['-title']
