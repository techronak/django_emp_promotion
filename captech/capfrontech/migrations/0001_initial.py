# Generated by Django 2.2.1 on 2019-09-06 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, null=True)),
            ],
            options={
                'unique_together': {('dept_no', 'dept_name')},
            },
        ),
        migrations.CreateModel(
            name='employees',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField(null=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('hire_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('title', models.CharField(max_length=50, null=True)),
                ('from_date', models.DateField(primary_key=True, serialize=False)),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_title', to='capfrontech.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('salary', models.IntegerField(primary_key=True, serialize=False)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_salaries', to='capfrontech.employees')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='groups',
            field=models.ManyToManyField(to='capfrontech.Titles'),
        ),
        migrations.CreateModel(
            name='dept_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capfrontech.departments')),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_department', to='capfrontech.employees')),
            ],
        ),
    ]
