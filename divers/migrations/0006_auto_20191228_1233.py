# Generated by Django 2.2.4 on 2019-12-28 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divers', '0005_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Diver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='divers.Divers'),
        ),
        migrations.AddField(
            model_name='courses',
            name='tourphoto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]