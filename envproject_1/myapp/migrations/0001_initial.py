# Generated by Django 4.2.7 on 2023-12-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('PulicationDate', models.DateField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
