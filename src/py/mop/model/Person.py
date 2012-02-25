from google.appengine.ext import ndb

from mop.model import PostalAddress

"""A Person describes a "natural person" who will be taking one side or another
of a Parking Transaction.

A Person only exists as part of an Account, so we don't need to have a unique
index for them.
"""

class Person(ndb.Model):
  prefix = ndb.StringProperty()
  driversLicenseIssuer = ndb.StructuredProperty(PostalAddress.PostalAddress)
  first_names = ndb.StringProperty()
  last = ndb.StringProperty()
  suffix = ndb.StringProperty()
  driversLicense = ndb.StringProperty()
