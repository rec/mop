from google.appengine.ext import ndb

from mop.model import PostalAddress

"""A Person describes a "natural person" who will be taking one side or another
of a Parking Transaction.
"""

class Person(ndb.Model):
  id = ndb.IntegerProperty()

  prefix = ndb.StringProperty()
  driversLicenseIssuer = ndb.StructuredProperty(PostalAddress.PostalAddress)
  first_names = ndb.StringProperty()
  last = ndb.StringProperty()
  suffix = ndb.StringProperty()
  driversLicense = ndb.StringProperty()
