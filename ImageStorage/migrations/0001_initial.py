# Generated by Django 4.1.3 on 2022-11-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "input_img",
                    models.FileField(
                        blank=True, null=True, upload_to="input/", verbose_name="입력사진"
                    ),
                ),
                (
                    "output_img",
                    models.FileField(
                        blank=True, null=True, upload_to="output/", verbose_name="결과사진"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
