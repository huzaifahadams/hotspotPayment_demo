# Generated by Django 4.0.1 on 2022-02-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_payment_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='payment_num',
            name='phone_num',
            field=models.CharField(max_length=12),
        ),
    ]
