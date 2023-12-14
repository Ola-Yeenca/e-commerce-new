# Generated by Django 5.0 on 2023-12-13 23:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='items.item')),
                ('members', models.ManyToManyField(related_name='conversations_as_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='communication.conversation')),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
