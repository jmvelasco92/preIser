# Generated by Django 2.1 on 2018-10-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181003_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
