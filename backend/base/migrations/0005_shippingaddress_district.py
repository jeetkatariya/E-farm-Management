# Generated by Django 3.2.7 on 2021-09-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_shippingaddress_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='district',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
