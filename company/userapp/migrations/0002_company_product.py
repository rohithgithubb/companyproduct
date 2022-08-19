# Generated by Django 4.0.4 on 2022-08-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Product',
            fields=[
                ('Product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=30)),
                ('Product_quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'Company_Product',
            },
        ),
    ]
