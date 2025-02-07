# Generated by Django 5.0.6 on 2024-07-14 12:49

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('idx', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Registration number')),
                ('role', models.CharField(choices=[(1, 'Administrative'), (2, 'Management staff'), (3, 'Business owner')], max_length=30, verbose_name='Admin role')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(verbose_name='Surname')),
                ('firstName', models.CharField(verbose_name='First Name')),
                ('address', models.CharField(verbose_name='Residential Address')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('origin', models.CharField(verbose_name='State of Origin')),
                ('nationality', models.CharField(verbose_name='Nationality')),
                ('religion', models.CharField(verbose_name='Religion')),
            ],
            options={
                'verbose_name': 'Candidate Information',
                'verbose_name_plural': 'Candidates Information',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=3000)),
                ('welcome', models.TextField(verbose_name='Homepage welcome address')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motto', models.CharField(max_length=50)),
                ('vision', models.TextField(verbose_name='School vision')),
                ('mission', models.TextField(verbose_name='School mission')),
                ('creed', models.TextField(verbose_name='School creed')),
                ('core_values', models.TextField(verbose_name='Core values')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Pre-School'), (2, 'Primary'), (3, 'Junior'), (4, 'Senior')], verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatePreviousSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, verbose_name='School name')),
                ('date_history', models.DateField(blank=True, verbose_name='Date')),
                ('qualification', models.CharField(blank=True, verbose_name='Qualification')),
                ('date_qualification', models.DateField(blank=True, verbose_name='Date')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_previous_school', to='core.candidateinfo')),
            ],
            options={
                'verbose_name': 'Candidate Previous School',
                'verbose_name_plural': 'Candidates Previous Schools',
            },
        ),
        migrations.CreateModel(
            name='ParentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_surname', models.CharField(verbose_name='Parent Surname')),
                ('parent_name', models.CharField(verbose_name='Parent First Name')),
                ('home_address', models.CharField(verbose_name='Home Address')),
                ('profession', models.CharField(verbose_name='Profession')),
                ('office_address', models.CharField(verbose_name='Office Address')),
                ('parent_religion', models.CharField(verbose_name='Religion')),
                ('email_address', models.CharField(verbose_name='Email Address')),
                ('relation', models.CharField(verbose_name='Relationship')),
                ('contact_number', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_parent', to='core.candidateinfo')),
            ],
            options={
                'verbose_name': 'Parent Details',
                'verbose_name_plural': 'Parents Details',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_history', models.TextField(verbose_name='School History')),
                ('school_owner_welcome_address', models.TextField(verbose_name='School Owner Welcome Address')),
                ('student_leadership', models.TextField()),
                ('staff_report', models.TextField(verbose_name='Our Staff')),
                ('result_report', models.TextField(verbose_name='Result and Honours Roll')),
                ('school_vision_and_mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.schoolvision')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Class name')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.section', verbose_name='Section')),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Registration number')),
                ('std_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.class', verbose_name='Class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Subject')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_subjects', to='core.section', verbose_name='Section')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='subjects',
            field=models.ManyToManyField(related_name='class_subjects', to='core.subject', verbose_name='Subjects'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('idx', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Registration number')),
                ('subjects', models.ManyToManyField(related_name='+', to='core.subject', verbose_name='Subject')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ManyToManyField(to='core.teacher', verbose_name='Teachers'),
        ),
    ]
