from django.http import HttpResponse
from ..models import Oms_user
from django.template import loader
from django.views import generic

__all__ = ['IndexView']

class IndexView(generic.ListView):
    template_name = 'oms/index.html'
    context_object_name = 'user_list'
    def get_queryset(self):
        """ return user list """
        return Oms_user.objects.all()



    # def index(request):
    #     template = loader.get_template('oms/index.html')
    #     user_list = Oms_user.objects.all()
    #     content = {
    #         'user_list' : user_list,
    #     }
    #     print(user_list[0].user_name)
    #     return HttpResponse(template.render(content, request))