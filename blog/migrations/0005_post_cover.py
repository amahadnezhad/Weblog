# Generated by Django 4.2.14 on 2024-07-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_post_alter_comment_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
