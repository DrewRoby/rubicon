from django.db import models
from django.contrib.auth.models import User
from players.models import PlayerGroup

# TypeError: unsupported operand type(s) for %: 'DeferredAttribute' and 'dict'
class Con(models.Model):
    CON_ID = models.AutoField(primary_key=True)
    CON_NAME = models.CharField(max_length=200)
    CON_TAGLINE = models.CharField(max_length=500)
    CON_OWNER = models.ForeignKey(User, related_name=User.username, on_delete=models.PROTECT)
    P_GROUP_ID = models.ForeignKey(PlayerGroup, related_name=PlayerGroup.P_GROUP_ID, on_delete=models.PROTECT)
    CON_BEGIN = models.DateTimeField()
    CON_END = models.DateTimeField(null=True)
    CREATE_DATE = models.DateTimeField()
    IS_PRIVATE = models.BooleanField(default=False)
    
    class Meta:
        unique_together = (('CON_ID','P_GROUP_ID'),)