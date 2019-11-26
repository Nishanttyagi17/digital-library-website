# Generated by Django 2.2.2 on 2019-11-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('Branch', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='notes/pdfs/')),
            ],
        ),
    ]
