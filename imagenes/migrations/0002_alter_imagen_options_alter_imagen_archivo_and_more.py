# Generated by Django 5.1.7 on 2025-03-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterField(
            model_name='imagen',
            name='archivo',
            field=models.ImageField(upload_to='imagenes/', verbose_name='Archivo de imagen'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre de la imagen'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='tipo_detectado',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo detectado'),
        ),
    ]
