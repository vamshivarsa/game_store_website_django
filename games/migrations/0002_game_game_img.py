# Generated by Django 3.0.4 on 2020-03-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_img',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
