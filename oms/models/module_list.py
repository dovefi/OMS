from django.db import models

# Create your models here.

__all__ = ['ModuleList']

# table filed content
VB_MODULE_LIST = {
    'vb_mn' : 'module name',
    'vb_mc' : 'module caption',
    'vb_me' : 'module extend',
}


# list of module
class ModuleList(models.Model):
    module_name    = models.CharField(max_length=20, verbose_name=VB_MODULE_LIST['vb_mn'])
    module_caption = models.CharField(max_length=255, verbose_name=VB_MODULE_LIST['vb_mc'])
    module_extend  = models.TextField(verbose_name=VB_MODULE_LIST['vb_me'])

    class Meta:
        pass











