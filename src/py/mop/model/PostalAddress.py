from google.appengine.ext import ndb

class PostalAddress(ndb.Model):
  id = ndb.IntegerProperty()

  intro = ndb.StringProperty()  # c/o John Smith
  unitNumber = ndb.StringProperty()  # Room 5
  streetNumber = ndb.StringProperty()  # 1600
  streetName = ndb.StringProperty()  # Pennsylvania Av NW
  city = ndb.StringProperty()  # Washington
  district = ndb.StringProperty()  # (rare in US)
  state = ndb.StringProperty()  # DC
  postalCode = ndb.StringProperty()  # 20500
  postalSubcode = ndb.StringProperty()  # Zip+4, e.g.
  country = ndb.StringProperty()  # USA
  notes = ndb.StringProperty()  # Won't be printed on envelopes...
