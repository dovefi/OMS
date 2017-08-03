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
    'vb_sn'  : 'server name',
    'vb_sw'  : 'server public network ip',
    'vb_sl'  : 'server inner network ip',
    'vb_so'  : 'OS of server',
    'vb_sai' : 'id of service application category',
}
VB_MODULE_LIST = {
    'vb_mn' : 'module name',
    'vb_mc' : 'module caption',
    'vb_me' : 'module extend',
}
VB_SERVER_HISTORY = {
    'vb_hid' : 'history id',
    'vb_hip' : 'history of the server',
    'vb_hu'  : 'history user',
    'vb_hd'  : 'happen date',
    'vb_dd'  : 'insert into db date',
    'vb_hc'  : 'history command',
}
VB_OMS_USER = {
    'vb_un'  : 'user name',
    'vb_up'  : 'user password',
    'vb_ue'  : 'user email',
    'vb_uct' : 'user create time',
}

# service function category
class Server_fun_categ(models.Model):
    server_categ_name = models.CharField(max_length=20, help_text=VB_SERVER_FUN_CATEG['vb_scn'])

# service application category
class Server_app_categ(models.Model):
    server_fun_categ = models.ForeignKey(Server_fun_categ, on_delete=models.CASCADE, help_text=VB_SERVER_APP_CATEG['vb_sci'])
    app_categ_name  = models.CharField(max_length=30, help_text=VB_SERVER_APP_CATEG['vb_acn'])

# list of servers
class Server_list(models.Model):
    server_name   = models.CharField(max_length=13, help_text=VB_SERVER_LIST['vb_sn'])
    server_wip    = models.CharField(max_length=15, help_text=VB_SERVER_LIST['vb_sw'])
    server_lip    = models.CharField(max_length=12, help_text=VB_SERVER_LIST['vb_sl'])
    server_op     = models.CharField(max_length=10, help_text=VB_SERVER_LIST['vb_so'])
    server_app_categ = models.ForeignKey(Server_app_categ, help_text=VB_SERVER_LIST['vb_sai'])

# list of module
class Module_list(models.Model):
    module_name    = models.CharField(max_length=20, help_text=VB_MODULE_LIST['vb_mn'])
    module_caption = models.CharField(max_length=255, help_text=VB_MODULE_LIST['vb_mc'])
    module_extend  = models.TextField(help_text=VB_MODULE_LIST['vb_me'])

# server history
class Server_history(models.Model):
    history_id       = models.IntegerField(help_text=VB_SERVER_HISTORY['vb_hid'])
    server_list      = models.ForeignKey(Server_list, help_text=VB_SERVER_HISTORY['vb_hip'])
    history_user     = models.CharField(max_length=15, help_text=VB_SERVER_HISTORY['vb_hu'])
    history_datetime = models.DateTimeField(help_text=VB_SERVER_HISTORY['vb_hd'])
    db_datetime      = models.DateTimeField(help_text=VB_SERVER_HISTORY['vb_dd'])
    history_command  = models.CharField(max_length=255, help_text=VB_SERVER_HISTORY['vb_hc'])

# oms user
class Oms_user(models.Model):
    user_name        = models.CharField(max_length=11, help_text=VB_OMS_USER['vb_un'])
    user_password    = models.CharField(max_length=15, help_text=VB_OMS_USER['vb_up'])
    user_email       = models.CharField(max_length=30, help_text=VB_OMS_USER['vb_ue'])
    user_create_time = models.DateTimeField(help_text=VB_OMS_USER['vb_uct'])
















