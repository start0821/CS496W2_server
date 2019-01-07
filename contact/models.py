from django.db import models
from user.models import Account

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,blank=False,null=True,default=None)

    def as_json(self):
        return dict(
        id=self.id, name=self.name,
        number=self.phone_number,
        account=self.account.pk)

    class Meta:
        ordering = ('account','name')
