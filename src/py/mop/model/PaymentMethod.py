from google.appengine.ext import ndb

from mop.model import PhoneNumber
from mop.model import PostalAddress

class PaymentMethod(ndb.Model):
  id = ndb.IntegerProperty()

  category = ndb.StringProperty()
  accountName = ndb.StringProperty()
  accountNumber = ndb.StringProperty()
  billingAddress = ndb.StructuredProperty(PostalAddress.PostalAddress)
  billingPhoneNumber = ndb.StructuredProperty(PhoneNumber.PhoneNumber)
