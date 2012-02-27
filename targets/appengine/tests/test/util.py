import testCase

from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import PhoneNumber
from mop.util import modelDict

PHONE_DICT = {'country':'USA', 'areaCode': '212', 'localNumber': '5551212'}


class RemoveNonesTestCase(testCase.TestCase):
  def testSimple(self):
    d = {'foo' : 1, 'bar': None}
    modelDict.removeNones(d)
    self.assertEqual(d, {'foo' : 1})

  def testSubdict(self):
    d = {'foo' : {'bar': None}}
    modelDict.removeNones(d)
    self.assertEqual(d, {'foo' : {}})

  def testComplex(self):
    d = {'foo' : {'bar': None, 'baz': False, 'bang': 0},
         'bing': None}
    r = modelDict.removeNones(d)
    self.assertEqual(d, {'foo' : {'baz': False, 'bang': 0}})


class ToDictTestCase(testCase.TestCase):
  def testSimple(self):
    number = PhoneNumber.PhoneNumber(**PHONE_DICT)
    d = modelDict.toDict(number)
    self.assertEqual(d, PHONE_DICT)

  def testComplex(self):
    m = {'category': 'VISA',
         'billingPhoneNumber': PHONE_DICT}
    phone = PhoneNumber.PhoneNumber(**PHONE_DICT)
    m2 = {'category': 'VISA',
         'billingPhoneNumber': phone}
    pay = PaymentMethod.PaymentMethod(**m2)
    d = modelDict.toDict(pay)
    self.assertEqual(d, {'category': 'VISA',
                         'billingPhoneNumber': PHONE_DICT})


class ToModelTestCase(testCase.TestCase):
  def testSimple(self):
    number = PhoneNumber.PhoneNumber()
    modelDict.toModel(number, PHONE_DICT)
    self.assertEqual(number, PhoneNumber.PhoneNumber(**PHONE_DICT))

  def testComplex(self):
    number = PhoneNumber.PhoneNumber()
    modelDict.toModel(number, {'country':'USA',
                               'areaCode': '212',
                         'localNumber': '5551212'})
    self.assertEqual(number, PhoneNumber.PhoneNumber(country='USA',
                                                     areaCode='212',
                                                     localNumber='5551212'))
"""

    d = pay.to_dict()
    fixDict(d)
    pay2 = PaymentMethod.PaymentMethod(billingPhoneNumber=phone)

    s = type(pay2).billingPhoneNumber
    s = isinstance(s, ndb.StructuredProperty) and 'yes' or 'no'
    s = isinstance(pay2.billingPhoneNumber, ndb.Model) and 'yes' or 'no'

    raise Exception(s)
    #raise Exception(d['accountName']);
"""
