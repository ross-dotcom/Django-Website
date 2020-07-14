from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'main.html'