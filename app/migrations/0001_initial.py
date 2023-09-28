# Generated by Django 4.2.3 on 2023-09-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('career', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Full Stack', 'Full Stack'), ('Intern', 'Intern')], max_length=50, null=True)),
            ],
        ),
    ]
