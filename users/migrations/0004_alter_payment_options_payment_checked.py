# Generated by Django 5.0.2 on 2024-11-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment_product_id_payment_product_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Оплата пользователя', 'verbose_name_plural': 'Оплаты пользователей'},
        ),
        migrations.AddField(
            model_name='payment',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Проверенная покупка'),
        ),
    ]
