from django.db import models

# Create your models here.


class IPFSFile(models.Model):
    name = models.CharField(max_length=255)
    ipfs_hash = models.TextField(default='{}')

    def __str__(self):
        return self.name