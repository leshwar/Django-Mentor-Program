# Generated by Django 2.2.6 on 2019-10-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_menteedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menteedata',
            old_name='isAvavilable',
            new_name='isAvailable',
        ),
        migrations.RenameField(
            model_name='mentordata',
            old_name='isAvavilable',
            new_name='isAvailable',
        ),
        migrations.AlterField(
            model_name='menteeregistrationdata',
            name='mentee_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mentorregistrationdata',
            name='mentor_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
