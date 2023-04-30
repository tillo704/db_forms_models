from django.db import models



# Create your models here.
class User(models.Model):
    user_id =  models.BigIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)    
    email = models.EmailField()
    about = models.TextField(null=True,blank=True)
    is_married = models.BooleanField(default=False)
    birthday = models.DateField()   
 
    


