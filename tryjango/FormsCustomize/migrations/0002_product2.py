# Generated by Django 2.0 on 2019-08-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsCustomize', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
        ),
    ]