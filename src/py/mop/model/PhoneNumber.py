from google.appengine.ext import ndb

class PhoneNumber(ndb.Model):
  country = ndb.StringProperty()
  areaCode = ndb.StringProperty()
  localNumber = ndb.StringProperty()
