from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "menu/index.html"
