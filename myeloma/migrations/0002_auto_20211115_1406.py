# Generated by Django 3.0.8 on 2021-11-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myeloma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='folder-2/')),
            ],
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to='folder-1/'),
        ),
    ]
