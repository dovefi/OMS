from django.db import models
from .server_app_categ import ServerAppCateg

VB_SERVER_LIST = {
    'vb_sn'  : 'server name',
    'vb_sw'  : 'server public network ip',
    'vb_sl'  : 'server inner network ip',
    'vb_so'  : 'OS of server',
    'vb_sai' : 'id of service application category',
}

# list of servers
class ServerList(models.Model):
    server_name      = models.CharField(max_length=13, verbose_name=VB_SERVER_LIST['vb_sn'])
    server_wip       = models.CharField(max_length=15, verbose_name=VB_SERVER_LIST['vb_sw'])
    server_lip       = models.CharField(max_length=12, verbose_name=VB_SERVER_LIST['vb_sl'])
    server_op        = models.CharField(max_length=10, verbose_name=VB_SERVER_LIST['vb_so'])
    server_app_categ = models.ForeignKey(ServerAppCateg, verbose_name=VB_SERVER_LIST['vb_sai'])

    class Meta:
        pass