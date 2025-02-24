from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from core.models import Feature

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        features = Feature.objects.filter(is_active=True)
        context = super().get_context_data(**kwargs)
        context['features'] = features

        return context
