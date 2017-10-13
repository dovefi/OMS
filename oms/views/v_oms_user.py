# from django.http import HttpResponse
from ..models import OmsUser
# from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from ..forms import *
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import login as auto_login, logout as auto_logout
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

__all__ = ['IndexView',
           'CreateUserView',
           'CreateUser',
           'LoginUserView',
           'LogoutUserView',
           ]

def CreateUser(request):
    print("request.path: {0}" .format(request.path))
    print("request.method:{0}" .format(request.method))
    if request.method == "GET":
        return render(request, 'oms/oms_user_create.html')
    elif request.method == "POST":
        form = UserCreateUpdateForm(request.POST)
        if form.is_valid():
            logger.info("create user {0}:" .format(request.POST['username']))
            model = OmsUser()
            model.set_password(request.POST['password'])
            model.email = request.POST['email']
            model.username = request.POST['username']
            model.save()
            return HttpResponseRedirect('/oms')
        else:
            logger.warning("form is invalid error {0}:" .format(form.errors))
            errors = {'errors' : form.errors}
            res = {'form' : form}
        return render(request, 'oms/oms_user_create.html', res)


class IndexView(generic.ListView):
    template_name = 'oms/index.html'
    context_object_name = 'user_list'
    logger.info("get user list success !")

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect("oms:login")
        else:
            return super(IndexView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        """ return user list """
        return OmsUser.objects.all()


# @login_required
class CreateUserView(CreateView):
    model = OmsUser
    form_class = UserCreateUpdateForm
    success_url = reverse_lazy('oms:index')
    template_name = 'oms/oms_user_create.html'

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


class LoginUserView(FormView):
    """
    user login view
    """
    template_name = 'oms/oms_user_login.html'
    success_url = reverse_lazy('oms:index')
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect(self.get_success_url())
        return super(LoginUserView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        auto_login(self.request, form.get_user())
        # auto_login(self.request)
        print(self.request.session)
        return redirect(self.get_success_url())


class LogoutUserView(generic.TemplateView):
    template_name = 'oms/oms_user_login.html'
    def get(self, request, *args, **kwargs):
        auto_logout(request)
        return super(LogoutUserView, self).get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = {
    #         'title': 'Logout success',
    #         'messages': 'Logout success, return login page',
    #         'redirect_url': reverse('oms:login'),
    #         'auto_redirect': True,
    #     }
    #     kwargs.update(context)
    #     return super(LogoutUserView, self).get_context_data(**kwargs)



