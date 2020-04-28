from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'    
    
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'
    
class WikiPageView(TemplateView):
    template_name = 'wiki.html'
    
class BlogPageView(TemplateView):
    template_name = 'blog.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'