# Generated by Django 4.0.3 on 2022-04-05 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('SAT', 'Sat'), ('GPA', 'Gpa')], max_length=10)),
                ('completed', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
        migrations.CreateModel(
            name='Sat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_test_score', models.FloatField()),
                ('private_tutor_time', models.FloatField()),
                ('have_a_strategy', models.BooleanField(default=False)),
                ('goal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sat', to='base.goal')),
            ],
        ),
        migrations.CreateModel(
            name='Gpa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_gpa', models.FloatField()),
                ('library_hours', models.FloatField()),
                ('friends_with_high_gpa', models.FloatField()),
                ('office_hours', models.FloatField()),
                ('goal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gpa', to='base.goal')),
            ],
        ),
    ]
