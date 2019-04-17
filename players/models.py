from django.db import models
from django.contrib.auth.models import User
from games import Game

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



# Is this the right place to put the player group?  Or just as good a place as any?
# Or should I leverage django's built-in groups?
class Player_Group(models.Model):
    PLAYER_P_GROUP_ID = models.CharField(max_length=500)
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    P_GROUP_ID = models.IntegerField()

class Library(models.Model):
    class Meta:
        unique_together = ((username,game_id),)

    username = models.ForeignKey(User, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
