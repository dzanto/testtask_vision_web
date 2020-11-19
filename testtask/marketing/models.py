from django.db import models


class Card(models.Model):
    name = models.CharField(
        max_length=10,
        default='img',
        verbose_name='Открытка'
    )
    img_file = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name
