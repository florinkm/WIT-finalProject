# Generated by Django 4.2 on 2023-06-06 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_alter_alamatpengiriman_options_payment_order_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkategori', models.CharField(choices=[('DL', 'Detergent Laundry'), ('AN', 'Anti Noda'), ('PL', 'Pelengkap Laundry'), ('ML', 'Mesin Laundry')], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toko.category'),
        ),
    ]
