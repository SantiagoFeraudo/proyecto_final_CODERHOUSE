from django.shortcuts import render
from .models import Project
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from porfolio.forms import RegisterForm

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects}) 

class UserRegistration(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('porfolio:success')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration,self).form_valid(form)

