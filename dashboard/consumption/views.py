from django.db.models import Prefetch, Sum
from django.views.generic import DetailView, ListView

from .models import Consumption, UserData


class summary(ListView):
    template_name = 'consumption/summary.html'
    model = UserData
    query_set = model.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(summary, self).get_context_data(**kwargs)
        context['consumption'] = UserData.objects.annotate(
            total_consumption=Sum('users__consumption')
        )
        return context


class detail(DetailView):
    template_name = 'consumption/detail.html'
    model = UserData