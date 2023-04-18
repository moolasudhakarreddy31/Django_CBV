from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse


# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse("<h1>This is class based views </h1>")


class HelloWorldTemplateView(TemplateView):
    template_name='cbvapp/results.html'



class HelloWorldTemplateViewContext(TemplateView):
    template_name='cbvapp/info.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="SudhakarReddy"
        context['subject']="Python"
        context['marks']=100
        return context