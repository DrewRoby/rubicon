from django.db import models

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
    __tablename__ = 'PLAYER_GROUP'

    PLAYER_P_GROUP_ID = models.CharField(max_length=500)
    PLAYER_ID = models.Column(models.Integer, ForeignKey(PLAYER.PLAYER_ID), nullable = False)
    P_GROUP_ID = models.Column(models.Integer)