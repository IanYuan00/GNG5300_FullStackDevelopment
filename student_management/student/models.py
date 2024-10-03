from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    geade = models.CharField(max_length=2)

    def __str__(self):
        return self.first_name + ' ' + self.last_name