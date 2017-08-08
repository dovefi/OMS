from django.db import models
from django.contrib.auth.models import AbstractUser

VB_OMS_USER = {
    'vb_un'   : 'user name',
    'vb_up'   : 'user password',
    'vb_ue'   : 'user email',
    'vb_uct'  : 'user create time',
    'vb_ulmt' : 'user last modify time',
}


# oms user
class Oms_user(models.Model):
    user_name             = models.CharField(max_length=11, verbose_name=VB_OMS_USER['vb_un'])
    user_password         = models.CharField(max_length=15, verbose_name=VB_OMS_USER['vb_up'])
    user_email            = models.CharField(max_length=30, verbose_name=VB_OMS_USER['vb_ue'])
    user_create_time      = models.DateTimeField(auto_now_add=True, verbose_name=VB_OMS_USER['vb_uct'])
    user_last_modify_time = models.DateTimeField(auto_now=True, verbose_name=VB_OMS_USER['vb_ulmt'])

    class Meta:
        pass

    @property
    def getUserName(self):
        return self.user_name

    def setUserName(self, user_name):
        self.user_name = user_name

    def setPassword(self, password):
        self.user_password = password

    def resetPassword(self, password):
        self.user_password = password
        self.save()

    @property
    def getEmail(self):
        return self.user_email

    def setEmail(self, email):
        self.user_email = email

