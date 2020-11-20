# Generated by Django 3.1.3 on 2020-11-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('logo', 'Логотип'), ('head_pic', 'Изображение в шапке'), ('card1', 'Первая открытка'), ('card2', 'Вторая открытка'), ('card3', 'Третья открытка'), ('card4', 'Четвертая открытка'), ('realization_pic', 'Открытка в реализации')], max_length=15)),
                ('img_file', models.ImageField(upload_to='img/')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('hello', 'Приветствие'), ('text01', 'Изображение в шапке'), ('text02', 'Первая открытка'), ('text03', 'Вторая открытка'), ('text04', 'Третья открытка'), ('cooperation', 'Сотрудничество'), ('email', 'e-mail')], max_length=15)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
        migrations.AddConstraint(
            model_name='text',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_text'),
        ),
        migrations.AddConstraint(
            model_name='pic',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_pic'),
        ),
    ]