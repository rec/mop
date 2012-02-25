import datetime
import time

from google.appengine.api import datastore_types

TYPE_FUNCTIONS = {}

def getTypeFunction(value)
  f = TYPE_FUNCTIONS.get(type(value), None)
  if f:
    return f

  for t, f in TYPE_FUNCTIONS.items():
    if isinstance(value, t):
      return f

def modelToJSON(model):
  output = {}

  for key, prop in model.properties().iteritems():
    value = getattr(model, key)
    f = getTypeFunction(value)
    if not f:
      raise ValueError("Can't encode " + type(value))
    output[key] = f(value)

  return output

def identity(value):
  return value;

def datetimeToJSON(value):
  ms = time.mktime(value.utctimetuple()) * 1000
  us = getattr(value, 'microseconds', 0) / 1000
  return int(ms + us)

def geoPtToJSON(value):
  return {'lat': value.lat, 'lon': value.lon}

def imToJSON(value):
  return {'address': value.address, 'protocol': value.protocol}

TYPE_FUNCTIONS = {
  ndb.Model: modelToJSON,
  datastore_types.GeoPt: geoPtToJSON
  datastore_types.IM: imToJSON
  datetime.date: datetimeToJSON,

  int: identity,
  long: identity,
  float: identity,
  bool: identity,
  dict: identity,
  basestring: identity,
  list: identity,
  type(None): identity,
  }
