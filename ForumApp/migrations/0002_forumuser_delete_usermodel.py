# Generated by Django 4.2.4 on 2023-08-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForumApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=32)),
                ('user_image', models.ImageField(blank=True, default='', null=True, upload_to='static/img')),
                ('user_details', models.TextField(blank=True, default='', max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
