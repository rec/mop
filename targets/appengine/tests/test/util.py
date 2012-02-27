import testCase

from google.appengine.ext import ndb

from mop.model import PaymentMethod
from mop.model import PhoneNumber
from mop.util import modelDict


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
    number = PhoneNumber.PhoneNumber(country='USA',
                                     areaCode='212',
                                     localNumber='5551212')
    d = modelDict.toDict(number)
    self.assertEqual(d, {'country':'USA',
                         'areaCode': '212',
                         'localNumber': '5551212'})


  def testComplex(self):
    p = {'country':'USA',
         'areaCode': '212',
         'localNumber': '5551212'}
    m = {'category': 'VISA',
         'billingPhoneNumber': p}
    phone = PhoneNumber.PhoneNumber(**p)
    m2 = {'category': 'VISA',
         'billingPhoneNumber': phone}
    pay = PaymentMethod.PaymentMethod(**m2)
    d = modelDict.toDict(pay)
    self.assertEqual(d, {'category': 'VISA',
                         'billingPhoneNumber': {'areaCode': '212',
                                                'country': 'USA',
                                                'localNumber': '5551212'}})



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
