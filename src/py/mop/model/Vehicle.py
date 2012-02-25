from google.appengine.ext import ndb

class Vehicle(ndb.Model):
  category = ndb.StringProperty()
  length = ndb.FloatProperty()
  axles = ndb.IntegerProperty()
  make = ndb.StringProperty()
  model = ndb.StringProperty()
  year = ndb.IntegerProperty()
  description = ndb.StringProperty()
  registration_number = ndb.StringProperty()
