# Generated by Django 2.1.7 on 2019-03-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='物品名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.CharField(max_length=40, verbose_name='使用人'),
        ),
    ]