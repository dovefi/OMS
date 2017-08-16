from django.db import models
from django.contrib.auth.models import AbstractUser

VB_OMS_USER = {
    'vb_un'   : 'user name',
    'vb_ue'   : 'user email',
    'vb_wc'   : 'user wechat'
}

__all__ = ['OmsUser']

# oms user
class OmsUser(AbstractUser):
    username = models.CharField(max_length=11, unique=True, blank=False, verbose_name=VB_OMS_USER['vb_un'])
    email = models.EmailField(max_length=30, unique=True, blank=True, verbose_name=VB_OMS_USER['vb_ue'])
    wechat = models.CharField(max_length=20, blank=True, verbose_name=['vb_wc'])
    class Meta:
        pass


