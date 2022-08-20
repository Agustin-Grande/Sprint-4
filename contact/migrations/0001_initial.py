# Generated by Django 4.0.5 on 2022-07-17 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0002_alter_project_options_project_image_project_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField(default=datetime.date.today)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]