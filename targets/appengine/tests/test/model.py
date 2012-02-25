from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

import testCase

from mop.model import PhoneNumber
from mop.model import PostalAddress
from mop.model import Vehicle

class DemoTestCase(testCase.TestCase):
  def _initStubs(self, testbed):
    testbed.init_datastore_v3_stub()
    testbed.init_memcache_stub()

  def doTestClass(self, constructor, **kw):
    number = constructor(**kw)
    number2 = number.put().get()
    self.assertEqual(number, number2)

  def testPhoneNumber(self):
    self.doTestClass(PhoneNumber.PhoneNumber, country='USA')

  def testPostalAddress(self):
    self.doTestClass(PostalAddress.PostalAddress, unit_number='1R')

  def testVehicle(self):
    self.doTestClass(Vehicle.Vehicle, category='sedan')

if __name__ == '__main__':
    unittest.main()
