# Generated by Django 4.1.3 on 2022-12-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50, null=True)),
                ('patientname', models.CharField(max_length=50, null=True)),
                ('doc_email', models.EmailField(max_length=50, null=True)),
                ('patient_email', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('symptoms', models.CharField(max_length=50, null=True)),
                ('prescriptions', models.CharField(max_length=50, null=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('middlename', models.CharField(max_length=200, null=True)),
                ('birthday', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=12, null=True)),
                ('experience', models.CharField(max_length=3, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('education', models.CharField(max_length=3, null=True)),
                ('departament', models.CharField(max_length=200, null=True)),
                ('specialization', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('photo', models.FileField(null=True, upload_to='images/')),
                ('working_hours', models.JSONField(default=list, null=True)),
                ('duration', models.CharField(max_length=5, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
