from google.appengine.ext import ndb

class PhoneNumber(ndb.Model):
  id = ndb.IntegerProperty()

  country = ndb.StringProperty()
  areaCode = ndb.StringProperty()
  localNumber = ndb.StringProperty()
