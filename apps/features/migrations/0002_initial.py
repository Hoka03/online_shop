# Generated by Django 5.0.6 on 2024-05-12 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeature',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='featurevalue',
            unique_together={('feature', 'value_uz')},
        ),
    ]