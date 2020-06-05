from django.db import models
import uuid
#from multi_email_field.fields import MultiEmailField

# Create your models here.
class email_model(models.Model):
    uid=models.CharField(max_length=200,default=uuid.uuid1(),auto_created=True)
    user=models.CharField(max_length=500,blank=True,null=True)
    recipients=models.CharField(max_length=2000,null=True,blank=True)
    #recipients=MultiEmailField(null=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    body=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.uid
