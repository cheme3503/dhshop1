# Generated by Django 4.1.4 on 2023-01-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0005_coupon_use_from_coupon_use_to_alter_coupon_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]