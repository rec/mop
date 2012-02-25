from google.appengine.ext import ndb

from mop.model import PostalAddress

"""A Person describes a "natural person" who will be taking one side or another
of a Parking Transaction.

A Person only exists as part of an Account, so we don't need to have a unique
index for them.
"""

class Person(ndb.Model):
  prefix = ndb.StringProperty()
  drivers_license_issuer = ndb.StructuredProperty(PostalAddress.PostalAddress)

"""
class Person(ndb.Model):
  string prefix = 1;  # Mr.
  repeated string name = 2;  # John Wellington Wells
  optional string suffix = 3;  # Esq.

  optional string drivers_license = 4;
  optional PostalAddress drivers_license_issuer = 5;
};
"""
