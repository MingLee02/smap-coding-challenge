import factory

from ..models import Consumption, UserData
 

class UserDataFactory(factory.DjangoModelFactory):
    user_id = factory.Sequence('id {}'.format)
    area = factory.Sequence('area {}'.format)
    tariff = factory.Sequence('tariff {}'.format)

    class Meta:
        model = UserData


class ConsumptionFactory(factory.DjangoModelFactory):
    datetime = factory.LazyFunction(datetime.now)
    consumption = factory.Sequence('consumption {}'.format)

    class Meta:
        model = Consumption