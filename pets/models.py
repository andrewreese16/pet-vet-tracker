from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pet(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=50)
  breed = models.CharField(max_length=50, blank=True, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
class Visit(models.Model):
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
  reason = models.CharField(max_length=255)
  visit_date = models.DateField()

  def __str__(self):
    return f"{self.reason} - {self.pet.name}"
  
  