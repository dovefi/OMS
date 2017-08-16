from django.db import models
from .server_list import ServerList

VB_SERVER_HISTORY = {
    'vb_hid' : 'history id',
    'vb_hip' : 'history of the server',
    'vb_hu'  : 'history user',
    'vb_hd'  : 'happen date',
    'vb_dd'  : 'insert into db date',
    'vb_hc'  : 'history command',
}

# server history
class ServerHistory(models.Model):
    history_id       = models.IntegerField(verbose_name=VB_SERVER_HISTORY['vb_hid'])
    server_list      = models.ForeignKey(ServerList, verbose_name=VB_SERVER_HISTORY['vb_hip'])
    history_user     = models.CharField(max_length=15, verbose_name=VB_SERVER_HISTORY['vb_hu'])
    history_datetime = models.DateTimeField(verbose_name=VB_SERVER_HISTORY['vb_hd'])
    db_datetime      = models.DateTimeField(verbose_name=VB_SERVER_HISTORY['vb_dd'])
    history_command  = models.CharField(max_length=255, verbose_name=VB_SERVER_HISTORY['vb_hc'])

    class Meta:
        pass