from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from ecosystems.models import Ecosystem

# Create your models here.
class Grant(models.Model):
    class ProjectCategory(models.TextChoices):
        ALL = 'All'
        AI = 'AI'
        ANALYTICS = 'Analytics'
        BRIDGESANDINTEROPERABILITY = 'Bridges / Interoperability'
        CEX = 'CEX'
        COMMUNITIES = 'Communities'
        CONTENT = 'Content'
        DEFI = 'DeFi'
        DERIVATIVES = 'Derivatives'
        DEX = 'Dex'
        FOUNDATION = 'Foundation'
        GAMEFI = 'GameFi'
        GRANTS = 'Grants'
        INDEX = 'Index'
        INFRASTRUCTURE = 'Infrastructure'
        INSURANCE = 'Insurance'
        IOT = 'IOT'
        LAYER1 = 'Layer 1'
        LAYER2 = 'Layer 2'
        LENDANDBORROW = 'Lend / Borrow'
        METAGOVERNANCE = 'Metagovernance'
        MUSIC = 'Music'
        NFT = 'NFT'
        ORACLES = 'Oracles'
        PRIVACY = 'Privacy'
        PROTOCOLDAO = 'Protocol DAO'
        QUADRATICFUNDING = 'Quadratic Funding'
        RESEARCH = 'Research'
        SOCIAL = 'Social'
        SOCIALCAUSES = 'Social Causes'
        STABLECOIN = 'Stable Coin'
        STAKING = 'Staking'
        YIELDFARMING = 'Yield Farming'

    class GrantType(models.TextChoices):
        ALL = 'All'
        ANALYTICS = 'Analytics'
        COMMUNITY = 'Community'
        CONTENT = 'Content'
        DEVELOPMENT = 'Development'
        OTHER = 'Other'

    ecosystem = models.ForeignKey(Ecosystem, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    website = models.CharField(max_length=150, blank=True)
    bounties = models.CharField(max_length=150, blank=True)
    forum = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    grant_details =models.CharField(max_length=150)
    description = models.TextField(blank=True)
    project_category = models.CharField(max_length=50, choices=ProjectCategory.choices, default=ProjectCategory.ALL)
    grant_type = models.CharField(max_length=50, choices=GrantType.choices, default=GrantType.ALL)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title