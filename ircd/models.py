from django.db import models

class IrcServer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    port = models.IntegerField()
    rpc_url = models.URLField()
    rpc_user = models.CharField(max_length=100, default='User')
    rpc_password = models.CharField(max_length=100, default='default')  # Set a default value here
