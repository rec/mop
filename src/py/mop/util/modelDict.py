import copy
import datetime
import time

from google.appengine.api import datastore_types
from google.appengine.ext import ndb

def removeNones(d):
  toDel = []
  deletes = 0
  for k, v in d.iteritems():
    if v is None:
      toDel.append(k)

    elif isinstance(v, dict):
      removeNones(v)

  for k in toDel:
    del d[k]


def toDict(model):
  d = model.to_dict()
  removeNones(d)
  return d


def toModel(model, d):
  modelType = type(model)
  for key, value in d.iteritems():
    modelProperty = getattr(modelType, key)
    if isinstance(modelProperty, ndb.StructuredProperty):
      modelValue = modelProperty._modelclass()
      toModel(modelValue, value)
      value = modelValue

    setattr(model, key, value)
