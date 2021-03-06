from django.db import models
from .server_fun_categ import ServerFunCateg

__all__ = ['ServerAppCateg']

VB_SERVER_APP_CATEG = {
    'vb_sci' : 'foreign key,service function id,delete cascade ',
    'vb_acn' : 'name of service application category ',
}


# service application category
class ServerAppCateg(models.Model):
    server_fun_categ = models.ForeignKey(ServerFunCateg, on_delete=models.CASCADE, verbose_name=VB_SERVER_APP_CATEG['vb_sci'])
    app_categ_name = models.CharField(max_length=30, verbose_name=VB_SERVER_APP_CATEG['vb_acn'])

    class Meta:
        pass