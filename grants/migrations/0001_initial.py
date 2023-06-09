# Generated by Django 4.2 on 2023-04-25 21:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ecosystems", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grant",
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
                ("slug", models.CharField(max_length=200, unique=True)),
                ("title", models.CharField(max_length=150)),
                ("website", models.CharField(blank=True, max_length=150)),
                ("bounties", models.CharField(blank=True, max_length=150)),
                ("forum", models.CharField(blank=True, max_length=150)),
                ("twitter", models.CharField(blank=True, max_length=150)),
                ("grant_details", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                (
                    "project_category",
                    models.CharField(
                        choices=[
                            ("All", "All"),
                            ("AI", "Ai"),
                            ("Analytics", "Analytics"),
                            (
                                "Bridges / Interoperability",
                                "Bridgesandinteroperability",
                            ),
                            ("CEX", "Cex"),
                            ("Communities", "Communities"),
                            ("Content", "Content"),
                            ("DeFi", "Defi"),
                            ("Derivatives", "Derivatives"),
                            ("Dex", "Dex"),
                            ("Foundation", "Foundation"),
                            ("GameFi", "Gamefi"),
                            ("Grants", "Grants"),
                            ("Index", "Index"),
                            ("Infrastructure", "Infrastructure"),
                            ("Insurance", "Insurance"),
                            ("IOT", "Iot"),
                            ("Layer 1", "Layer1"),
                            ("Layer 2", "Layer2"),
                            ("Lend / Borrow", "Lendandborrow"),
                            ("Metagovernance", "Metagovernance"),
                            ("Music", "Music"),
                            ("NFT", "Nft"),
                            ("Oracles", "Oracles"),
                            ("Privacy", "Privacy"),
                            ("Protocol DAO", "Protocoldao"),
                            ("Quadratic Funding", "Quadraticfunding"),
                            ("Research", "Research"),
                            ("Social", "Social"),
                            ("Social Causes", "Socialcauses"),
                            ("Stable Coin", "Stablecoin"),
                            ("Staking", "Staking"),
                            ("Yield Farming", "Yieldfarming"),
                        ],
                        default="All",
                        max_length=50,
                    ),
                ),
                (
                    "grant_type",
                    models.CharField(
                        choices=[
                            ("All", "All"),
                            ("Analytics", "Analytics"),
                            ("Community", "Community"),
                            ("Content", "Content"),
                            ("Development", "Development"),
                            ("Other", "Other"),
                        ],
                        default="All",
                        max_length=50,
                    ),
                ),
                (
                    "main_photo",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                ("is_published", models.BooleanField(default=True)),
                (
                    "date_added",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "ecosystem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="ecosystems.ecosystem",
                    ),
                ),
            ],
        ),
    ]
