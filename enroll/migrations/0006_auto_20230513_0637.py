# Generated by Django 3.2.12 on 2023-05-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_contact_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub1', models.CharField(max_length=100)),
                ('sub2', models.CharField(max_length=100)),
                ('sub3', models.CharField(max_length=100)),
                ('sub4', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
    ]