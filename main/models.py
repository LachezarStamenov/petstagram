import datetime

from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Model

from main.validators import only_letters_validator

# UserModel = get_user_model()

class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH), only_letters_validator)
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH), only_letters_validator)
    )

    picture = models.URLField()

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True
    )


class Pet(models.Model):
    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    # TYPES = ((x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)), not a tuple comprehension, generator

    MAX_LENGTH = 30

    name = models.CharField(max_length=MAX_LENGTH)

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        )

    # One-to-one relations

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(

        )
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(auto_now_add=True,)

    likes = models.IntegerField(default=0,)

    tagged_pets = models.ManyToManyField(Pet,) # validate at least 1 pet

    # user = models.ForeignKey(
    #     Profile,
    #     on_delete=models.CASCADE,
    # )

