import requests
import json

from django.views import generic
from django.views.generic import TemplateView

from interface.forms import *


class ProcedureList(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super(ProcedureList, self).get_context_data(**kwargs)

        r = requests.get('http://127.0.0.1:8000/api/procedure/')

        context['prueba'] = r.text

        return context


class ProcedureDetail(TemplateView):
    template_name = 'test.html'

    def get(self, request, id, *args, **kwargs):
        kwargs['id'] = id

        return super(ProcedureDetail, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProcedureDetail, self).get_context_data(**kwargs)

        r = requests.get('http://127.0.0.1:8000/api/procedure/'+str(kwargs['id']))

        context['prueba'] = r.text

        return context


# class StepCreate(generic.FormView):
#     """
#         docstring for ProcedureCreateView
#     """
#     template_name = 'test.html'
#     form_class = StepCreateForm
#     success_url = '/thanks/'


# class StepUpdate(generic.FormView):

#     template_name = 'test.html'
#     form_class = StepUpdateForm
#     success_url = '/thanks/'

#     def get(self, *args, **kwargs):
#         r = requests.get('http://127.0.0.1:8000/api/procedure/'+str(kwargs['id']))
#         print r.json()
#         for key, value in r.json().items():
#             self.initial[key] = value
#         self.initial['id'] = kwargs['id']
#         return super(ProcedureUpdate, self).get(self, *args, **kwargs)


# class StepDelete(generic.FormView):

#     template_name = 'delete.html'
#     form_class = StepDeleteForm
#     success_url = '/thanks'

#     def get(self, *args, **kwargs):
#         self.initial['id'] = kwargs['id']
#         return super(ProcedureDelete, self).get(self, *args, **kwargs)
