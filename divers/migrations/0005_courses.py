# Generated by Django 2.2.4 on 2019-12-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divers', '0004_auto_20191015_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thetype', models.CharField(max_length=50)),
                ('requirment', models.CharField(max_length=50)),
            ],
        ),
    ]
