# from django.http import HttpResponse
from ..models import OmsUser
from ..forms import UserForm
# from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

__all__ = ['IndexView',
           'CreateUserView',
           'CreateUser',
           ]

def CreateUser(request):
    print("request.path: {0}" .format(request.path))
    print("request.method:{0}" .format(request.method))
    if request.method == "GET":
        return render(request, 'oms/oms_user_create.html')
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            model = OmsUser()
            model.setEmail(request.POST['user_email'])
            model.setPassword(request.POST['user_password'])
            model.setUserName(request.POST['user_name'])
            model.save()
            return HttpResponseRedirect('/oms')
        else:
            errors = {'errors' : form.errors}
            res = {'form' : form}
        return render(request, 'oms/oms_user_create.html', res)

class IndexView(generic.ListView):
    template_name = 'oms/index.html'
    context_object_name = 'user_list'
    logger.info("get user list success !")

    def get_queryset(self):
        """ return user list """
        return OmsUser.objects.all()


class CreateUserView(CreateView):
    model = OmsUser
    fields = '__all__'
    success_url = reverse_lazy('oms:index')
    template_name = 'oms_user_create.html'
    # template_name_suffix = '_create'

    # def post(self, request, *args, **kwargs):
    #     logger.info(request)
    # def login(request):
    #     template = loader.get_template('oms/index.html')
    #     user_list = Oms_user.objects.all()
    #     content = {
    #         'user_list' : user_list,
    #     }
    #     print(user_list[0].user_name)
    #     return HttpResponse(template.render(content, request))
