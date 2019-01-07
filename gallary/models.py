from django.db import models
from user.models import Account
import os

# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to="gallary/%Y/%m/%d")
    owner = models.ForeignKey(Account,on_delete=models.CASCADE)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension
