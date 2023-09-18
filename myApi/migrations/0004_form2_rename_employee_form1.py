# Generated by Django 4.2.4 on 2023-09-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0003_rename_name_employee_firstname_employee_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0, max_length=12)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='Form1',
        ),
    ]