# Generated by Django 2.2 on 2019-12-14 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery_images', verbose_name='Фото')),
                ('signature', models.CharField(max_length=200, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('like_amount', models.IntegerField(default=0, verbose_name='Лайк')),
                ('author', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='photos_author', to=settings.AUTH_USER_MODEL, verbose_name='Кто добавил')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='comments_photo', to='webapp.Photo', verbose_name='Фотография')),
            ],
        ),
    ]
