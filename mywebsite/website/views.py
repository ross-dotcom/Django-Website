from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'
