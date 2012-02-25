from google.appengine.ext import ndb

class PostalAddress(ndb.Model):
  intro = ndb.StringProperty()  # c/o John Smith
  unit_number = ndb.StringProperty()  # Room 5
  street_number = ndb.StringProperty()  # 1600
  street_name = ndb.StringProperty()  # Pennsylvania Av NW
  city = ndb.StringProperty()  # Washington
  district = ndb.StringProperty()  # (rare in US)
  state = ndb.StringProperty()  # DC
  postal_code = ndb.StringProperty()  # 20500
  postal_subcode = ndb.StringProperty()  # Zip+4, e.g.
  country = ndb.StringProperty()  # USA
  notes = ndb.StringProperty()  # Won't be printed on envelopes...
