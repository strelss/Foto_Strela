# Generated by Django 2.2.4 on 2019-10-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_Famyly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_img1', models.ImageField(upload_to='')),
                ('fam_img2', models.ImageField(upload_to='')),
                ('fam_img3', models.ImageField(upload_to='')),
                ('fam_img4', models.ImageField(upload_to='')),
                ('fam_img5', models.ImageField(upload_to='')),
                ('fam_img6', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_Portrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_img1', models.ImageField(upload_to='')),
                ('port_img2', models.ImageField(upload_to='')),
                ('port_img3', models.ImageField(upload_to='')),
                ('port_img4', models.ImageField(upload_to='')),
                ('port_img5', models.ImageField(upload_to='')),
                ('port_img6', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_Weding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wed_img1', models.ImageField(upload_to='')),
                ('wed_img2', models.ImageField(upload_to='')),
                ('wed_img3', models.ImageField(upload_to='')),
                ('wed_img4', models.ImageField(upload_to='')),
                ('wed_img5', models.ImageField(upload_to='')),
                ('wed_img6', models.ImageField(upload_to='')),
            ],
        ),
    ]
