# Generated by Django 2.0.6 on 2018-10-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_material_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cantidad',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
