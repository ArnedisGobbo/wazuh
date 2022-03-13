import unittest

from app import create_app, db
from app.api.models.users import User, Geo, Address, Company
from app.api.models.tasks import Task


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            BaseTestClass.create_user(1, 'Leanne Graham', 'Bret', 'Sincere@april.biz', 'Kulas Light', 'Apt. 556',
                                      'Gwenborough', '92998-3874', '-37.3159', '81.1496', '1-770-736-8031 x56442',
                                      'hildegard.org', 'Romaguera-Crona', 'Multi-layered client-server neural-net',
                                      'harness real-time e-markets')
            BaseTestClass.create_task(1, 1, 'delectus aut autem', False)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @staticmethod
    def create_user(_id, name, username, email, address_street, address_suite, address_city, address_zipcode,
                    address_geo_lat, address_geo_lng, phone, website, company_name, company_catch_phrase,
                    company_bs):
        geo = Geo(lat=address_geo_lat,
                  lng=address_geo_lng)

        address = Address(street=address_street,
                          suite=address_suite,
                          city=address_city,
                          zipcode=address_zipcode,
                          geo=geo)

        company = Company(name=company_name,
                          catch_phrase=company_catch_phrase,
                          bs=company_bs)

        user = User(_id=_id,
                    name=name,
                    username=username,
                    email=email,
                    address=address,
                    phone=phone,
                    website=website,
                    company=company,
                    )

        user.save()
        return user

    @staticmethod
    def create_task(_id, user_id, title, completed):
        task = Task(_id=_id,
                    user_id=user_id,
                    title=title,
                    completed=completed,
                    )

        task.save()
        return task
