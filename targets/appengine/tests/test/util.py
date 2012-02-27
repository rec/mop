import testCase

from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import PhoneNumber
from mop.util import modelDict

PHONE_DICT = {'country':'USA', 'areaCode': '212', 'localNumber': '5551212'}
PAY_DICT = {'category': 'VISA', 'billingPhoneNumber': PHONE_DICT}


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
    phone = PhoneNumber.PhoneNumber(**PHONE_DICT)
    pay = PaymentMethod.PaymentMethod(category='VISA',
                                      billingPhoneNumber=phone)
    d = modelDict.toDict(pay)
    self.assertEqual(d, PAY_DICT)


class ToModelTestCase(testCase.TestCase):
  def testSimple(self):
    number = PhoneNumber.PhoneNumber()
    modelDict.toModel(number, PHONE_DICT)
    self.assertEqual(number, PhoneNumber.PhoneNumber(**PHONE_DICT))

  def testComplex(self):
    pay = PaymentMethod.PaymentMethod()
    modelDict.toModel(pay, PAY_DICT)
    phone = PhoneNumber.PhoneNumber(**PHONE_DICT)
    self.assertEqual(pay,
                     PaymentMethod.PaymentMethod(category='VISA',
                                                 billingPhoneNumber=phone))
