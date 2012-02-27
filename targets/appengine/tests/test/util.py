import testCase

from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import PhoneNumber
from mop.util import ModelDict

PHONE_DICT = {'country':'USA', 'areaCode': '212', 'localNumber': '5551212'}
PAY_DICT = {'category': 'VISA', 'billingPhoneNumber': PHONE_DICT}


class RemoveNonesTestCase(testCase.TestCase):
  def testSimple(self):
    d = {'foo' : 1, 'bar': None}
    ModelDict.removeNones(d)
    self.assertEqual(d, {'foo' : 1})

  def testSubdict(self):
    d = {'foo' : {'bar': None}}
    ModelDict.removeNones(d)
    self.assertEqual(d, {'foo' : {}})

  def testComplex(self):
    d = {'foo' : {'bar': None, 'baz': False, 'bang': 0},
         'bing': None}
    r = ModelDict.removeNones(d)
    self.assertEqual(d, {'foo' : {'baz': False, 'bang': 0}})


class ToDictTestCase(testCase.TestCase):
  def testSimple(self):
    number = PhoneNumber.PhoneNumber(**PHONE_DICT)
    d = ModelDict.toDict(number)
    self.assertEqual(d, PHONE_DICT)

  def testComplex(self):
    phone = PhoneNumber.PhoneNumber(**PHONE_DICT)
    pay = PaymentMethod.PaymentMethod(category='VISA',
                                      billingPhoneNumber=phone)
    d = ModelDict.toDict(pay)
    self.assertEqual(d, PAY_DICT)


class ToModelTestCase(testCase.TestCase):
  def testSimple(self):
    number = PhoneNumber.PhoneNumber()
    ModelDict.toModel(number, PHONE_DICT)
    self.assertEqual(number, PhoneNumber.PhoneNumber(**PHONE_DICT))

  def testComplex(self):
    pay = PaymentMethod.PaymentMethod()
    ModelDict.toModel(pay, PAY_DICT)
    phone = PhoneNumber.PhoneNumber(**PHONE_DICT)
    p2 = PaymentMethod.PaymentMethod(category='VISA', billingPhoneNumber=phone)
    self.assertEqual(pay, p2)
