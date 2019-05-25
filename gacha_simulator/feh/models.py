from django.db import models


# Create your models here.
class Heroes(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    )

    TYPE_RED = 'red'
    TYPE_BLUE = 'blue'
    TYPE_GREEN = 'green'
    TYPE_COLORLESS = 'colorless'
    TYPE_CHOICES = (
        (TYPE_RED, 'red'),
        (TYPE_BLUE, 'blue'),
        (TYPE_GREEN, 'green'),
        (TYPE_COLORLESS, 'colorless'),
    )

    WEAPON_SWORD = 'sword'
    WEAPON_LANCE = 'lance'
    WEAPON_AXE = 'axe'
    WEAPON_RED_BOW = 'red_bow'
    WEAPON_BLUE_BOW = 'blue_bow'
    WEAPON_GREEN_BOW = 'green_bow'
    WEAPON_COLORLESS_BOW = 'colorless_bow'
    WEAPON_RED_TOME = 'red_tome'
    WEAPON_BLUE_TOME = 'blue_tome'
    WEAPON_GREEN_TOME = 'green_tome'
    WEAPON_RED_DRAGGER = 'red_dragger'
    WEAPON_BLUE_DRAGGER = 'blue_dragger'
    WEAPON_GREEN_DRAGGER = 'green_dragger'
    WEAPON_COLORLESS_DRAGGER = 'colorless_dragger'
    WEAPON_RED_BREATH = 'red_breath'
    WEAPON_BLUE_BREATH = 'blue_breath'
    WEAPON_GREEN_BREATH = 'green_breath'
    WEAPON_COLORLESS_BREATH = 'colorless_breath'
    WEAPON_RED_BEAST = 'red_beast'
    WEAPON_BLUE_BEAST = 'blue_beast'
    WEAPON_GREEN_BEAST = 'green_beast'
    WEAPON_COLORLESS_BEAST = 'colorless_beast'
    WEAPON_STAFF = 'staff'
    WEAPON_CHOICES = (
        (WEAPON_SWORD, 'sword'),
        (WEAPON_LANCE, 'lance'),
        (WEAPON_AXE, 'axe'),
        (WEAPON_RED_BOW, 'red_bow'),
        (WEAPON_BLUE_BOW, 'blue_bow'),
        (WEAPON_GREEN_BOW, 'green_bow'),
        (WEAPON_COLORLESS_BOW, 'colorless_bow'),
        (WEAPON_RED_TOME, 'red_tome'),
        (WEAPON_BLUE_TOME, 'blue_tome'),
        (WEAPON_GREEN_TOME, 'green_tome'),
        (WEAPON_RED_DRAGGER, 'red_dragger'),
        (WEAPON_BLUE_DRAGGER, 'blue_dragger'),
        (WEAPON_GREEN_DRAGGER, 'green_dragger'),
        (WEAPON_COLORLESS_DRAGGER, 'colorless_dragger'),
        (WEAPON_RED_BREATH, 'red_breath'),
        (WEAPON_BLUE_BREATH, 'blue_breath'),
        (WEAPON_GREEN_BREATH, 'green_breath'),
        (WEAPON_COLORLESS_BREATH, 'colorless_breath'),
        (WEAPON_RED_BEAST, 'red_beast'),
        (WEAPON_BLUE_BEAST, 'blue_beast'),
        (WEAPON_GREEN_BEAST, 'green_beast'),
        (WEAPON_COLORLESS_BEAST, 'colorless_beast'),
        (WEAPON_STAFF, 'staff'),
    )

    MOVE_INFANTRY = 'infantry'
    MOVE_CAVALRY = 'cavalry'
    MOVE_ARMORED = 'armored'
    MOVE_FLYING = 'flying'
    MOVE_CHOICES = (
        (MOVE_INFANTRY, 'infantry'),
        (MOVE_CAVALRY, 'cavalry'),
        (MOVE_ARMORED, 'armored'),
        (MOVE_FLYING, 'flying'),
    )

    COLOR_WEAPON_MAPPING = {
        TYPE_RED: [WEAPON_SWORD, WEAPON_RED_BOW, WEAPON_RED_DRAGGER, WEAPON_RED_TOME, WEAPON_RED_BREATH,
                   WEAPON_RED_BEAST],
        TYPE_BLUE: [WEAPON_LANCE, WEAPON_BLUE_BOW, WEAPON_BLUE_DRAGGER, WEAPON_BLUE_TOME, WEAPON_BLUE_BREATH,
                    WEAPON_BLUE_BEAST],
        TYPE_GREEN: [WEAPON_AXE, WEAPON_GREEN_BOW, WEAPON_GREEN_DRAGGER, WEAPON_GREEN_TOME, WEAPON_GREEN_BREATH,
                     WEAPON_GREEN_BEAST],
        TYPE_COLORLESS: [WEAPON_STAFF, WEAPON_COLORLESS_BOW, WEAPON_COLORLESS_DRAGGER, WEAPON_COLORLESS_BREATH,
                         WEAPON_COLORLESS_BEAST]
    }

    name = models.CharField(max_length=64, default=None, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None, null=True)
    rarity_low = models.IntegerField(default=None, null=True)
    rarity_high = models.IntegerField(default=None, null=True)
    hero_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=None, null=True)
    weapon_type = models.CharField(max_length=32, default=None, null=True)
    move_type = models.CharField(max_length=16, default=None, null=True)
    appears_in = models.CharField(max_length=128, default=None, null=True)
    voice_actor = models.CharField(max_length=32, default=None, null=True)
    art_by = models.CharField(max_length=32, default=None, null=True)
    release_date = models.DateTimeField(default=None, null=True)
    description = models.TextField(default=None, null=True)
    health = models.IntegerField(default=None, null=True)
    attack = models.IntegerField(default=None, null=True)
    speed = models.IntegerField(default=None, null=True)
    defense = models.IntegerField(default=None, null=True)
    resistance = models.IntegerField(default=None, null=True)
    image = models.CharField(max_length=128, default=None, null=True)


class Pools(models.Model):
    name = models.CharField(max_length=128, default=None, null=True)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)
    start5_focus = models.DecimalField(decimal_places=6, max_digits=18, default=None, null=True)
    start5 = models.DecimalField(decimal_places=6, max_digits=18, default=None, null=True)
    start4 = models.DecimalField(decimal_places=6, max_digits=18, default=None, null=True)
    start3 = models.DecimalField(decimal_places=6, max_digits=18, default=None, null=True)
    heroes = models.ManyToManyField(Heroes)
