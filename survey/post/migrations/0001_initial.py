# Generated by Django 3.0.6 on 2020-07-03 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('na', 'N/A')], max_length=100)),
                ('age', models.CharField(choices=[('0 - 17', '0 - 17'), ('18 - 24', '18 - 24'), ('25 - 34', '25 - 34'), ('35 - 44', '35 - 44'), ('45 - 54', '45 - 54'), ('55 - 64', '55 - 64'), ('65 or more', '65 or more')], max_length=100)),
                ('income', models.CharField(choices=[('$0 - $24,999', '$0 - $24,999'), ('$25,000 - $49,999', '$25,000 - $49,999'), ('$50,000 - $74,999', '$50,000 - $74,999'), ('$75,000 - $99,999', '$75,000 - $99,999'), ('$100,000 - $149,999', '$100,000 - $149,999'), ('$150,000 or more', '$150,000 or more')], max_length=100)),
                ('education', models.CharField(choices=[('Less than HS diploma', 'Less than HS diploma'), ('High school', 'High school'), ('Some college', 'Some college'), ('Bachelors degree', 'Bachelors degree'), ('Graduate degree', 'Graduate degree')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]