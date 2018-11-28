from django.db import models
from django.contrib.auth.models import User

class Bets(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length = 100,null=True)
    money = models.PositiveIntegerField()
    bet_date = models.DateTimeField(auto_now_add=True)

    def save_bets(self):
        self.save()

    def delete_bets(self):
        self.delete()

    @classmethod
    def get_all(cls):
        bets = cls.objects.all()
        return bets

class UserProfile(models.Model):
    user_image = models.ImageField(upload_to = 'profile_pic/',null=True)
    username = models.CharField(max_length =30)
    bio = models.TextField(max_length = 100,null=True)


    def save_userprofile(self):
        self.save()

    def delete_userprofile(self):
        self.delete()
