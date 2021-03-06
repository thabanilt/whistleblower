# Generated by Django 2.1.4 on 2018-12-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('by', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='complain',
            name='by',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='complain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comportal.Complain'),
        ),
    ]
