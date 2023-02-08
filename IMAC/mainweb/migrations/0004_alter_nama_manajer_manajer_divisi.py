# Generated by Django 4.1 on 2023-02-04 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0003_auto_20230202_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nama_manajer',
            name='manajer',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisi', models.CharField(blank=True, choices=[('IR', 'Metallurgy'), ('SD', 'Material'), ('ER', 'Mineral'), ('RP', 'Mining'), ('WD', 'Extractive'), ('CR', 'Coal'), ('MD', 'Manufacture'), ('CC', 'Excavator'), ('FU', 'Pyrometallurgy'), ('SP', 'Blast Furnace')], default='oo', help_text='Asal Divisi', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
