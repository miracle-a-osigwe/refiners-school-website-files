# Generated by Django 5.0.6 on 2024-07-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_updateimage_img_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateimage',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
