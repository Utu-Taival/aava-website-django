from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"