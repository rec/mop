from google.appengine.ext import ndb

class Vehicle(ndb.Model):
  id = ndb.IntegerProperty()

  category = ndb.StringProperty()
  length = ndb.FloatProperty()
  axles = ndb.IntegerProperty()
  make = ndb.StringProperty()
  model = ndb.StringProperty()
  year = ndb.IntegerProperty()
  description = ndb.StringProperty()
  registrationNumber = ndb.StringProperty()
