# Generated by Django 5.0.6 on 2024-05-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]