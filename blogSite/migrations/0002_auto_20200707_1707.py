# Generated by Django 3.0.8 on 2020-07-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True)),
                ('email', models.EmailField(max_length=1000, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=2000000, null=True),
        ),
    ]
