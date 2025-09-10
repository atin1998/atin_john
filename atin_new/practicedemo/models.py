from django.db import models

# Create your models here.


class Member(models.Model):
    first_name=models.CharField(max_length=22,blank=True,null=True)
    last_name=models.CharField(max_length=23,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)

    class Meta:
        db_table='member'

