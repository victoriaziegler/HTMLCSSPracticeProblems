from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    pronouns = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey("Person", related_name="pets", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
