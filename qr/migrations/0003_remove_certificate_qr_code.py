# Generated by Django 5.1.5 on 2025-02-04 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_certificate_qr_code_alter_certificate_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='qr_code',
        ),
    ]
