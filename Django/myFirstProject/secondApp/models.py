from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadd = models.CharField(max_length=30)

    def __str__(self):
        return 'Employee Object With eno: ' + str(self.eno)
