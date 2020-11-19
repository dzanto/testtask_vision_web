from django.db import models


class Card(models.Model):
    img_file = models.ImageField(upload_to='marketing/static/img/')
