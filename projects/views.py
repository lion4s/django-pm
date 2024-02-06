from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms
class ProjectListViews(ListView):
    models=models.Project
    template_name = 'project/list.html'

class ProjrctsCreateViews(CreateView):
    model=models.Project
    form_class = forms.projectCreatForms
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')




