import testCase

from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import PhoneNumber
from mop.util import modelDict


class UtilTestCase(testCase.TestCase):
  def testPhoneNumber(self):
    p = {'country':'USA',
         'areaCode': '212',
         'localNumber': '5551212'}
    number = PhoneNumber.PhoneNumber(**p)
    self.assertEqual(p, number.to_dict())

  def testRemoveNones(self):
    d = {'foo' : 1, 'bar': None}
    modelDict.removeNones(d)
    self.assertEqual(d, {'foo' : 1})

  def testRemoveNones2(self):
    d = {'foo' : {'bar': None}}
    modelDict.removeNones(d)
    self.assertEqual(d, {'foo' : {}})

  def XtestRemoveNones(self):
    d = {'foo' : {'bar': None, 'baz': False, 'bang': 0},
         'bing': None}
    r = modelDict.removeNones(d)
    self.assertEqual(r, 1)
    self.assertEqual(d, {'foo' : {'baz': False, 'bang': 0}})

"""
    p = {'country':'USA',
         'areaCode': '212',
         'localNumber': '5551212'}
    m = {'category': 'VISA',
         'billingPhoneNumber': p}
    phone = PhoneNumber.PhoneNumber(**p)
    m2 = {'category': 'VISA',
         'billingPhoneNumber': phone}
    pay = PaymentMethod.PaymentMethod(**m2)

    d = pay.to_dict()
    fixDict(d)
    pay2 = PaymentMethod.PaymentMethod(billingPhoneNumber=phone)

    s = type(pay2).billingPhoneNumber
    s = isinstance(s, ndb.StructuredProperty) and 'yes' or 'no'
    s = isinstance(pay2.billingPhoneNumber, ndb.Model) and 'yes' or 'no'

    raise Exception(s)
    #raise Exception(d['accountName']);
"""
