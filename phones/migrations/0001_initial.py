# Generated by Django 3.0.6 on 2020-05-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('RegDate', models.DateTimeField(verbose_name='date published')),
                ('Address', models.CharField(max_length=255)),
                ('PhoneNumber', models.CharField(max_length=30)),
            ],
        ),
    ]
