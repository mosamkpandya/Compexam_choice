# Generated by Django 4.0 on 2024-08-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enrollment_no', models.CharField(max_length=50)),
                ('branch', models.CharField(choices=[('CE', 'Computer Engineering'), ('IT', 'Information Technology'), ('CSE', 'Computer Science Engineering'), ('CSD', 'Computer Science and Design'), ('AIML', 'Artificial Intelligence and Machine Learning'), ('AIDS', 'Artificial Intelligence and Data Science'), ('RAI', 'Robotics and AI'), ('CSIT', 'Computer Science and Information Technology'), ('CST', 'Computer Science and Technology')], max_length=10)),
                ('contact_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('choices', models.CharField(choices=[('GPSC', 'GPSC'), ('UPSC', 'UPSC'), ('GATE', 'GATE'), ('OTHER', 'Other Competitive Exam')], max_length=20)),
            ],
        ),
    ]
