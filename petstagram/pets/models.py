from django.core.exceptions import ValidationError
from django.db import models


def is_limited(value):
    if value > 120:
        raise ValidationError("Age is out of range 0-120.")


# Create your models here.
class Pet(models.Model):
    """
    type – some of the following: "cat", "dog", "parrot"; max length = 6
    name – max length = 6
    age – positive number
    description – text field
    image_url – URL field
    """
    # Animal_Choices = (
    #     ('cat', 'Cat'),
    #     ('dog', 'Dog'),
    #     ('parrot', 'Parrot'),
    # )
    # The first element in each tuple is the actual value to be set on the model,
    # and the second element is the human-readable name

    # or define a suitably-named constant for each value:
    # can test pet.type == Pet.TYPE_CHOICE_CAT
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot'),
    )
    # class attributes
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(max_length=6)
    age = models.PositiveSmallIntegerField(
        validators=[
            is_limited,
            # models.Max(120),
        ]
    )
    description = models.TextField()
    image_url = models.URLField()

    # URLField = CharField(max 200) + validation for url

    # can use property but nit instance attributes
    @property
    def name_and_age(self):
        return f'{self.name}/{self.age}'

    def __str__(self):
        return self.name_and_age


class Like(models.Model):
    """
    pet – foreign key to a Pet One-to-many 1pet-> many likes
    """
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
