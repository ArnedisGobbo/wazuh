from marshmallow import fields, post_dump

from app.ext import ma


class UserSchema(ma.Schema):
    class Meta:
        ordered = True

    id = fields.Integer()
    name = fields.String()
    username = fields.String()
    email = fields.String()
    address = fields.Nested('AddressSchema')
    phone = fields.String()
    website = fields.String()
    company = fields.Nested('CompanySchema')

    @post_dump(pass_many=True)
    def build_response(self, data, many):
        resp = {}
        if many is True:
            resp["total_items"] = len(data)

        resp["data"] = data

        return resp


class AddressSchema(ma.Schema):
    class Meta:
        ordered = True

    street = fields.String()
    suite = fields.String()
    city = fields.String()
    zipcode = fields.String()
    geo = fields.Nested('GeoSchema')


class GeoSchema(ma.Schema):
    class Meta:
        ordered = True

    lat = fields.String()
    lng = fields.String()


class CompanySchema(ma.Schema):
    class Meta:
        ordered = True

    name = fields.String()
    catch_phrase = fields.String(data_key="catchPhrase")
    bs = fields.String()
