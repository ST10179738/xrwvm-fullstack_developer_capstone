from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Optional field to track creation date
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID referring to Cloudant DB
    dealer_id = models.IntegerField(default=1)

    name = models.CharField(max_length=100)

    # Limited choices for Car Type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # Year constrained between 2015 and 2023
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
