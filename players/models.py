from django.db import models
from django.contrib.auth.models import User
from games.models import Game

# class Profile(models.Model):

    #Add any additional profile bits we need beyond the standard auth.user (shouldn't be anything, but...)
    #Also, the below receivers will automatically update the Profile when a User is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class PlayerGroup(models.Model):
    PLAYER_P_GROUP_ID = models.CharField(primary_key=True, max_length=500)
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    P_GROUP_ID = models.IntegerField()

class Library(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
