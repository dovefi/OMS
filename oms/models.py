from django.db import models

# Create your models here.

# table filed content
VB_SERVER_FUN_CATEG = {
    'vb_scn' : 'name of service function category ',
}
VB_SERVER_APP_CATEG = {
    'vb_sci' : 'foreign key,service function id,delete cascade ',
    'vb_acn' : 'name of service application category ',
}
VB_SERVER_LIST = {
    'vb_sn' : 'server name',
    'vb_sw' : 'server public network ip',
    'vb_sl' : 'server inner network ip',
    'vb_so' : 'OS of server',
    'vb_sai' : 'id of service application category',
}
VB_MODULE_LIST = {
    'vb_mn' : 'module name',
    'vb_mc' : 'module caption',
    'vb_me' : 'module extend',
}

# service function category
class Server_fun_categ(models.Model):
    server_categ_name = models.CharField(max_length=20, verbose_name=VB_SERVER_FUN_CATEG['vb_scn'])

# service application category
class Server_app_categ(models.Model):
    server_fun_categ = models.ForeignKey(Server_fun_categ, on_delete=models.CASCADE, verbose_name=VB_SERVER_APP_CATEG['vb_sci'])
    app_categ_name  = models.CharField(max_length=30, verbose_name=VB_SERVER_APP_CATEG['vb_acn'])

# list of servers
class Server_list(models.Model):
    server_name   = models.CharField(max_length=13, verbose_name=VB_SERVER_LIST['vb_sn'])
    server_wip    = models.CharField(max_length=15, verbose_name=VB_SERVER_LIST['vb_sw'])
    server_lip    = models.CharField(max_length=12, verbose_name=VB_SERVER_LIST['vb_sl'])
    server_op     = models.CharField(max_length=10, verbose_name=VB_SERVER_LIST['vb_so'])
    server_app_categ = models.ForeignKey(Server_app_categ, verbose_name=VB_SERVER_LIST['vb_sai'])

# list of module
class Module_list(models.Model):
    module_name    = models.CharField(max_length=20, verbose_name=VB_MODULE_LIST['vb_mn'])
    module_caption = models.CharField(max_length=255, verbose_name=VB_MODULE_LIST['vb_mc'])
    module_extend  = models.CharField(max_length=2000, verbose_name=VB_MODULE_LIST['vb_me'])















