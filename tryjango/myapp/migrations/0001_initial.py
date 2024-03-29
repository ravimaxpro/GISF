# Generated by Django 2.0 on 2019-08-13 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments1',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(max_length=120, null=True)),
                ('updated_by', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'departments1',
            },
        ),
        migrations.CreateModel(
            name='employees1',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_uid', models.CharField(max_length=120, null=True, unique=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=25)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=3, null=True)),
                ('Date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_join', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('emp_age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(max_length=120, null=True)),
                ('updated_by', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'employees1',
            },
            managers=[
                ('all_employees', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=120)),
                ('dob', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='departments1',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.employees1'),
        ),
    ]
