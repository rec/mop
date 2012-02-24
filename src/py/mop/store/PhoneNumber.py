from google.appengine.ext import ndb

class PhoneNumber(ndb.Property):
  country = ndb.StringProperty()
  areaCode = ndb.StringProperty()
  localNumber = ndb.StringProperty()
