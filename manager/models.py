from django.db import models
from django.utils import timezone
from django.urls import reverse



# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    DOB = models.DateField()
    
    tested_date = models.DateField()

    TESTS = (
        ('ANTIGEN','ANTIGEN'),
        ('PCR','PCR')
    )

    STATUSES =(
        ('DEAD','DEAD'),
        ('TESTED_POSITIVE','POSITIVE'),
        ('QUARANTINED','QUARANTINED'),
    )

    test = models.CharField(max_length=10,choices=TESTS)
    status = models.CharField(max_length =17,choices=STATUSES)

    tel_no =models.CharField(max_length=10)

    address = models.TextField()


    def get_absolute_url(self):
        return reverse('manager:view_patient',
                args=[self.id])




    def __str__(self):
        return self.first_name+' '+self.last_name


    class Meta:
        ordering = ('-tested_date',)


