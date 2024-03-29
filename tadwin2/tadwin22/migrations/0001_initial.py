# Generated by Django 4.2.5 on 2024-02-09 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("userID", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("lastLoginDate", models.DateTimeField(auto_now=True)),
                ("registrationDate", models.DateTimeField(auto_now_add=True)),
                ("passwordHash", models.CharField(max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                ("noteID", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
                ("title", models.CharField(max_length=255)),
                ("wordcount", models.IntegerField()),
                ("creationDate", models.DateTimeField(auto_now_add=True)),
                ("version", models.IntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tadwin22.customuser",
                    ),
                ),
            ],
        ),
    ]
