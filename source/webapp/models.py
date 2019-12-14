from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery_images', null=True, blank=True, verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    like_amount = models.IntegerField(default=0, verbose_name='Лайк')
    author = models.ForeignKey(User, max_length=50, verbose_name='Кто добавил', related_name='photos_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.signature


class Comment(models.Model):
    text = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст')
    image = models.ForeignKey('webapp.Photo', max_length=200, verbose_name='Фотография', related_name='comments_photo', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, blank=False, related_name='comments_author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')



    def __str__(self):
        return self.text
