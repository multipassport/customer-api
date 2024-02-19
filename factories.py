from models import Customer

import factory

class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n + 1)
    name = 'John Doe'
    age = 12
    address = 'Moscow'
    description = 'Lorem ipsum dolorem est'

    class Meta:
        model = Customer
        sqlalchemy_session_persistence = 'commit'
