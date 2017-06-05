from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES,
        help_text="남자는 L쓰세요",
    )

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

