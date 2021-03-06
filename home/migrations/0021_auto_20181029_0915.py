# Generated by Django 2.0.6 on 2018-10-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20181025_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombre_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='numero_serie',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], default='Disponible', max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Nombre_Material'),
        ),
    ]
