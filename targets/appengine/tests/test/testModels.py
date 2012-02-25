from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

import testCase

from mop.store import PhoneNumber

class DemoTestCase(testCase.TestCase):
  def _initStubs(self, testbed):
    testbed.init_datastore_v3_stub()
    testbed.init_memcache_stub()

  def testInsertEntity(self):
    number = PhoneNumber.PhoneNumber(country='USA')
    key = number.put()
    number2 = key.get()
    self.assertEqual(number, number2)

if __name__ == '__main__':
    unittest.main()
