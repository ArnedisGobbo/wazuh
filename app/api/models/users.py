from app.db import db, BaseModelMixin


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    address = db.relationship('Address', backref='user', uselist=False)
    phone = db.Column(db.String)
    website = db.Column(db.String)
    company = db.relationship('Company', backref='user', uselist=False)
    tasks = db.relationship('Task', backref='user')

    def __init__(self, _id, name, username, email, address, phone, website, company):
        self.id = _id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def __repr__(self):
        return f'User({self.name})'

    def __str__(self):
        return f'{self.name}'


class Address(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String)
    suite = db.Column(db.String)
    city = db.Column(db.String)
    zipcode = db.Column(db.String)
    geo = db.relationship('Geo', backref='address', uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

    def __init__(self, street, suite, city, zipcode, geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo


class Geo(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String)
    lng = db.Column(db.String)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), unique=True)

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class Company(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    catch_phrase = db.Column(db.String)
    bs = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

    def __init__(self, name, catch_phrase, bs):
        self.name = name
        self.catch_phrase = catch_phrase
        self.bs = bs
