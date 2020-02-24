# Generated by Django 2.2.2 on 2020-02-23 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_diagnosis_medicalreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='visit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='visit.Visit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalreport',
            name='visit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='visit.Visit'),
            preserve_default=False,
        ),
    ]