# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_imagenesinicio_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesCertificados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to=b'imgCertificados')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
