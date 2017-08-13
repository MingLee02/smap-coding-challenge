import factory
import datetime

from ..models import Consumption, UserData
 

class UserDataFactory(factory.DjangoModelFactory):
    user_id = factory.Sequence('{}'.format)
    area = factory.Sequence('area {}'.format)
    tariff = factory.Sequence('tariff {}'.format)

    class Meta:
        model = UserData


class ConsumptionFactory(factory.DjangoModelFactory):
    datetime = factory.LazyFunction(datetime.datetime.now)
    consumption = factory.Sequence('consumption {}'.format)

    class Meta:
        model = Consumption