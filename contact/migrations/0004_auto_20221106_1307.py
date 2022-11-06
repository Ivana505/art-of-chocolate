# Generated by Django 3.2 on 2022-11-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]