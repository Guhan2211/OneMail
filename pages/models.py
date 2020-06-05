from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet=models.IntegerField(default=100,auto_created=True)
    temp_mail=models.IntegerField(default=0)
    temp_amnt=models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    

class pay_hist(models.Model):
    user =models.CharField(max_length=500)
    order_id=models.CharField(max_length=25)
    pay_id=models.CharField(max_length=25)
    amnt=models.IntegerField(default=0)
    date_ordered=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    