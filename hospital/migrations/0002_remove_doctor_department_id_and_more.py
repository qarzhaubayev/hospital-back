# Generated by Django 4.1.3 on 2022-11-30 11:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='homepage_url',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='iin_number',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialization_details_id',
        ),
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='date_of_birth',
            field=models.DateField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='price_of_appointment',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergancy_contact_number',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_number',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='iin_number',
            field=models.IntegerField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_num',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='ID_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='IIN_number',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(999999999999), django.core.validators.MinValueValidator(100000000000)]),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department_ID',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='homepage_URL',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization_details_ID',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]