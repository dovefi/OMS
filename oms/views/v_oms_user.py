from django.http import HttpResponse
from ..models import Oms_user
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

__all__ = ['IndexView',
           'CreateUserView',
           ]

class IndexView(generic.ListView):
    template_name = 'oms/index.html'
    context_object_name = 'user_list'
    def get_queryset(self):
        """ return user list """
        return Oms_user.objects.all()

class CreateUserView(CreateView):
    model = Oms_user
    fields ='__all__'
    success_url = reverse_lazy('oms:index')
    template_name_suffix = '_create'

    # def index(request):
    #     template = loader.get_template('oms/index.html')
    #     user_list = Oms_user.objects.all()
    #     content = {
    #         'user_list' : user_list,
    #     }
    #     print(user_list[0].user_name)
    #     return HttpResponse(template.render(content, request))
