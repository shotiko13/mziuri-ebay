# Generated by Django 5.1.4 on 2024-12-08 11:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=20, verbose_name="დასახელება")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                    "username",
                    models.CharField(max_length=100, verbose_name="იუზერნეიმი"),
                ),
                (
                    "first_name",
                    models.CharField(default="", max_length=100, verbose_name="სახელი"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="ელ.ფოსტის მისამართი"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="აქტიურია"),
                ),
            ],
            options={
                "verbose_name": "მომხმარებელი",
                "verbose_name_plural": "მომხმარებლები",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Cart",
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
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            12,
                            8,
                            11,
                            36,
                            28,
                            497630,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100, verbose_name="დასახელება")),
                ("description", models.TextField(verbose_name="აღწერა")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "listing_date",
                    models.DateField(
                        default=datetime.datetime(
                            2024,
                            12,
                            8,
                            11,
                            36,
                            28,
                            497107,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="content.category",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="content.customer",
                    ),
                ),
            ],
            options={
                "verbose_name": "პროდუქტი",
                "verbose_name_plural": "პროდუქტები",
                "ordering": ("listing_date",),
            },
        ),
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="content.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="content.product",
                    ),
                ),
            ],
        ),
    ]
