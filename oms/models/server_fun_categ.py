from django.db import models

# table filed content
VB_SERVER_FUN_CATEG = {
    'vb_scn' : 'name of service function category ',
}

# service function category
class ServerFunCateg(models.Model):
    server_categ_name = models.CharField(max_length=20, verbose_name=VB_SERVER_FUN_CATEG['vb_scn'])

    class Meta:
        pass