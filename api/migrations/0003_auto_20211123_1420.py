# Generated by Django 3.2.7 on 2021-11-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_state_enquiryform_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiryform',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='enquiryform',
            name='claimed_by',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
