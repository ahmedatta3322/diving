# Generated by Django 2.2.4 on 2019-10-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='divers',
            name='cert',
            field=models.CharField(default='Dive master', max_length=50),
        ),
        migrations.AddField(
            model_name='divers',
            name='email',
            field=models.EmailField(default='asd', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='divers',
            name='n_dives',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='divers',
            name='padi_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='divers',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='divers',
            name='user_name',
            field=models.CharField(default='asd', max_length=50),
            preserve_default=False,
        ),
    ]
