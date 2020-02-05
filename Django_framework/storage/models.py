from django.db import models

from fsas.CosmosMongo import _Users

# Create your models here.
class BlobBlockService(models.Model):
    """BlobBlockService model requires
    username, blob account, and container name
    """
    username = models.CharField("username", max_length = 255)
    blobaccount = models.CharField("blob account", max_length = 255)
    blobcontainer =  models.CharField("container name", max_length = 255)

    def __str__(self):
        return self.name