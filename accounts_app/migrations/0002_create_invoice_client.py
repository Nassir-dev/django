# Generated by Django 2.2.4 on 2019-08-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_invoice',
            name='client',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to='client_app.Client'),
        ),
    ]
