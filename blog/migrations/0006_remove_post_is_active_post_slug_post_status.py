# Generated by Django 4.2.14 on 2024-07-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_active',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=123456, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], default='pub', max_length=3),
        ),
    ]
