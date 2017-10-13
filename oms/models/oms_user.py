from django.db import models
from django.contrib.auth.models import AbstractUser

__all__ = ['OmsUser']

VB_OMS_USER = {
    'vb_un'   : 'user name',
    'vb_ue'   : 'user email',
    'vb_wc'   : 'user wechat'
}


# oms user
class OmsUser(AbstractUser):
    username = models.CharField(max_length=11, unique=True, blank=False, verbose_name=VB_OMS_USER['vb_un'])
    email = models.EmailField(max_length=30, unique=True, blank=True, verbose_name=VB_OMS_USER['vb_ue'])
    wechat = models.CharField(max_length=20, blank=True, verbose_name=['vb_wc'])

    class Meta:
        pass

    def __str__(self):
        return self.username


