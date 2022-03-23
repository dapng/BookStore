# Generated by Django 4.0.3 on 2022-03-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_books_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Выбранные книги на продажу')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество книг на продажу')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
            },
        ),
    ]
