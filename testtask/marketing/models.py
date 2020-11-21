from django.db import models


PIC_CHOICES = [
    ('logo', 'Логотип'),
    ('head_pic', 'Изображение в шапке'),
    ('card1', 'Первая открытка'),
    ('card2', 'Вторая открытка'),
    ('card3', 'Третья открытка'),
    ('card4', 'Четвертая открытка'),
    ('realization_pic', 'Открытка в реализации'),
]

PIC_NAME = {a: b for a, b in PIC_CHOICES}


class Pic(models.Model):
    name = models.CharField(
        max_length=15,
        choices=PIC_CHOICES,
    )

    img_file = models.ImageField(upload_to='img/')

    def __str__(self):
        return PIC_NAME[self.name]

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_pic')
        ]


TEXT_CHOICES = [
    ('hello', 'Приветствие'),
    ('text01', 'Текст 01'),
    ('text02', 'Текст 02'),
    ('text03', 'Текст 03'),
    ('text04', 'Текст 04'),
    ('cooperation', 'Сотрудничество'),
    ('email', 'e-mail'),
]

TEXT_NAME = {a: b for a, b in TEXT_CHOICES}


class Text(models.Model):
    name = models.CharField(
        max_length=15,
        choices=TEXT_CHOICES,
    )

    content = models.CharField(max_length=500)

    def __str__(self):
        return TEXT_NAME[self.name]

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_text')
        ]
