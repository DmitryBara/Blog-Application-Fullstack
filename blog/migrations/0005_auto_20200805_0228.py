# Generated by Django 3.0.8 on 2020-08-04 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200805_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='pub_date',
        ),
    ]
