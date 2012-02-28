from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import Person
from mop.model import PhoneNumber
from mop.model import PostalAddress
from mop.model import Vehicle

class Account(ndb.Model):
  id = ndb.IntegerProperty()
  googleAccountId = ndb.StringProperty()
  person = ndb.StructuredProperty(Person.Person, repeated=True)
  vehicle = ndb.StructuredProperty(Vehicle.Vehicle, repeated=True)
  paymentMethod = ndb.StructuredProperty(PaymentMethod.PaymentMethod,
                                         repeated=True)
  mailingAddress = ndb.StructuredProperty(PostalAddress.PostalAddress)
  phoneNumber = ndb.StructuredProperty(PhoneNumber.PhoneNumber)

