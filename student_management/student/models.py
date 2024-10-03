from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    grade = models.IntegerField()

    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.name()
    
