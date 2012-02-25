import unittest

from google.appengine.ext import testbed

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self._initStubs(self.testbed)

  def tearDown(self):
    self.testbed.deactivate()

  def _initStubs(self, testbed):
    pass
