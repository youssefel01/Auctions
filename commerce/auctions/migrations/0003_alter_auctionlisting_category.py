# Generated by Django 4.2.2 on 2023-08-16 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auctionlisting_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, related_name='categoryListings', to='auctions.category'),
        ),
    ]
