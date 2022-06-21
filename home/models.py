from django.db import models

# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name_plural = "Staff"

    first_name = models.CharField(max_length=254, unique=True)
    last_name = models.CharField(max_length=254)
    email_address = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=254)
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    gender = models.CharField(max_length=6, choices=GENDER, null=False)
    management_level_choices = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    management_level = models.CharField(
        max_length=26, choices=management_level_choices, null=False
    )
    position_held = models.CharField(max_length=254)
    basic_salary = models.IntegerField()

    def __str__(self):
        return self.first_name
