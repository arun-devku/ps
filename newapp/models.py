from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Logindetails(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Signup(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    user=models.ForeignKey(Logindetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class List(models.Model):
    content=models.CharField(max_length=300)
    user=models.ForeignKey(Logindetails,on_delete=models.CASCADE)