from django.db import models


class Books(models.Model):
    title = models.CharField('Название книги', max_length=250)
    image = models.URLField('Ссылка на обложку', null=True, blank=True)
    author = models.CharField('Автор книги', max_length=50)
    description = models.TextField('Описание книги', null=True, blank=True)
    price = models.IntegerField('Стоимость книги', null=True, blank=True)
    quantity = models.IntegerField('Количество книг', null=True, blank=True)
    sale = models.BooleanField('Продажа', default=False)
    quantity_sale = models.IntegerField('Количество книг на продажу', null=True, blank=True)


    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return f'/book/{self.id}'


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
