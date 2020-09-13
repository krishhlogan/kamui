from django.db import models
from django.utils.timezone import now

# Create your models here.


class IPFSFile(models.Model):
    name = models.CharField(max_length=255)
    ipfs_hash = models.TextField(default='{}')
    # #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    created_at = models.DateTimeField(default=now,blank=True)
    #
    # #updated_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(default=now,blank=True)

    def __str__(self):
        return self.name