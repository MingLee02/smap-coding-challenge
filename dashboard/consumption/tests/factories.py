import factory

from ..models import UserData
 

class UserDataFactory(factory.DjangoModelFactory):
    user_id = factory.Sequence('id {}'.format)
    area = factory.Sequence('area {}'.format)
    tariff = factory.Sequence('tariff {}'.format)

    class Meta:
        model = UserData