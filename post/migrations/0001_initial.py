# Generated by Django 5.0.6 on 2024-07-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.IntegerField(choices=[(1, 'about us summary'), (2, 'mission'), (3, 'vision'), (4, 'event'), (5, 'about us full'), (6, 'offer'), (7, 'creed'), (8, 'core values'), (9, 'school anthem')], default=4, verbose_name='Post category')),
                ('title', models.CharField(max_length=100, verbose_name='Post heading')),
                ('img', models.ImageField(blank=True, upload_to='images/', verbose_name='Insert image')),
                ('content', models.TextField(verbose_name='Add post content')),
                ('url', models.URLField(blank=True, verbose_name='Reference external links')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'School Post',
                'verbose_name_plural': 'School Posts',
            },
        ),
        migrations.CreateModel(
            name='UpdateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(default='', max_length=100, verbose_name='Image Title/Tag')),
                ('img_tag', models.TextField(max_length=500, verbose_name='Image Description')),
                ('img', models.ImageField(upload_to='images/', verbose_name='Select image')),
                ('img_use', models.IntegerField(choices=[(1, 'gallery'), (2, 'homepage'), (3, 'all'), (4, 'labs'), (5, 'reception'), (6, 'nursery/primary'), (7, 'secondary'), (8, 'classes'), (9, 'workshops'), (10, 'sports')], default=3, verbose_name='Page image assignment')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'School Image',
                'verbose_name_plural': 'School Images',
            },
        ),
    ]