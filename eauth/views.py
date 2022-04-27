from django.views.generic import CreateView, DetailView
from django.shortcuts import render

from eauth.forms import UserCreateForm
from eauth.models import UserProfile


class UserCreateView(CreateView):
    model = UserProfile
    success_url = "/"  # can be reverse_lazy in future
    form_class = UserCreateForm

'''
class ProfileView(DetailView):
    template_name = 'eauth/profile.html'
    model = UserProfile
    context_object_name = "userprofile"
    # pk_url_kwarg = 'id'
'''

def profile_view(request):
    context = {

    }
    return render(request, 'eauth/profile.html', context=context)