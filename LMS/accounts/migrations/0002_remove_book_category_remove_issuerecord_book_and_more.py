# Generated by Django 5.2.3 on 2025-06-25 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='issuerecord',
            name='book',
        ),
        migrations.RemoveField(
            model_name='issuerecord',
            name='member',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='IssueRecord',
        ),
    ]
