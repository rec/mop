from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

import testCase

from mop.store import PhoneNumber

class TestEntityGroupRoot(ndb.Model):
  """Entity group root"""
  pass

class DemoTestCase(testCase.TestCase):
  def _initStubs(self, testbed):
    testbed.init_datastore_v3_stub()
    testbed.init_memcache_stub()

  def testInsertEntity(self):
    PhoneNumber.PhoneNumber().put()
    # self.assertEqual(1, len(TestModel.all().fetch(2)))

if __name__ == '__main__':
    unittest.main()
