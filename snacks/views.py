from django.shortcuts import render
from django.views.generic import TemplateView # import template view first

# Create your views here.
# Now i Need To Create a class
class HomePage(TemplateView):
     template_name = 'home.html'

# create another class for about page
class AboutPage(TemplateView):
     template_name = 'about.html'