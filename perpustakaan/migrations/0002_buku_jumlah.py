# Generated by Django 4.2.1 on 2023-06-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jumlah',
            field=models.IntegerField(null=True),
        ),
    ]
