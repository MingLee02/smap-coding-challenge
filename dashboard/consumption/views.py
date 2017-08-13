from django.db.models import Prefetch
from django.views.generic import ListView

from .models import Consumption, UserData


class summary(ListView):
	template_name = 'consumption/summary.html'
	model = Consumption

	def get_queryset(self):
		return self.model.objects.all()

	def get_context_data(self, **kwargs):
		context = super(summary, self).get_context_data(**kwargs)
		context['users'] = UserData.objects.all()

		return context
  