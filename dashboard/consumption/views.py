from django.db.models import Prefetch, Sum
from django.views.generic import DetailView, ListView

from .models import Consumption, UserData


class summary(ListView):
    template_name = 'consumption/summary.html'
    model = UserData
    query_set = model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(summary, self).get_context_data(**kwargs)
        consumption = []

        for user in self.model.objects.all():
            total_consumption = Consumption.objects.filter(
                user=user
            ).aggregate(total=Sum('consumption'))

            consumption.append({
                'user': user,
                'consumption': total_consumption['total']
            })

        context['consumption'] = consumption
        return context


class detail(DetailView):
    pass