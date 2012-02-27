import testCase

from mop.model import Account
from mop.model import PaymentMethod
from mop.model import Person
from mop.model import PhoneNumber
from mop.model import PostalAddress
from mop.model import Vehicle

class ModelTestCase(testCase.TestCase):
  def doTestClass(self, constructor, **kw):
    number = constructor(**kw)
    number2 = number.put().get()
    self.assertEqual(number, number2)

  def testAccount(self):
    address = PostalAddress.PostalAddress(unitNumber='1R')
    phoneNumber = PhoneNumber.PhoneNumber()
    self.doTestClass(Account.Account,
                     mailingAddress=address,
                     phoneNumber=phoneNumber)

  def testPaymentMethod(self):
    address = PostalAddress.PostalAddress(unitNumber='1R')
    phoneNumber = PhoneNumber.PhoneNumber()
    self.doTestClass(PaymentMethod.PaymentMethod,
                     billingAddress=address,
                     billingPhoneNumber=phoneNumber)

  def testPerson(self):
    address = PostalAddress.PostalAddress(unitNumber='1R')
    self.doTestClass(Person.Person, driversLicenseIssuer=address)

  def testPhoneNumber(self):
    self.doTestClass(PhoneNumber.PhoneNumber, country='USA')

  def testPostalAddress(self):
    self.doTestClass(PostalAddress.PostalAddress, unitNumber='1R')

  def testVehicle(self):
    self.doTestClass(Vehicle.Vehicle, category='sedan')

if __name__ == '__main__':
    unittest.main()
