# Generated by Django 2.2.1 on 2019-06-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0003_auto_20190628_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='client',
            field=models.ForeignKey(default='cleared', on_delete='CASCADE', to='trucks.Client'),
        ),
    ]
