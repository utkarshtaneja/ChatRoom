# Generated by Django 5.1.2 on 2024-11-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.TextField(),
        ),
    ]