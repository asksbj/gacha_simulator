from django.db import models


# Create your models here.
class Heros(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
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
    name = models.CharField(max_length=64, default=None, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None, null=True)
    rarity = models.IntegerField(default=None, null=True)
    weapon_type = models.CharField(max_length=32, default=None, null=True)
