# Generated by Django 2.2.1 on 2019-06-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0006_auto_20190628_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='client',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='trucks.Client'),
        ),
    ]
