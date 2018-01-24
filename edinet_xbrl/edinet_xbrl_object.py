# coding: utf-8

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License. See accompanying LICENSE file.

from collections import OrderedDict
from edinet_xbrl.edinet_data_util import EdinetDataUtil


class EdinetData(object):
  def __init__(self, key, value, decimals=0, unit_ref="", context_ref=""):
    self.key = key
    self.value = value
    self.decimals = decimals
    self.unit_ref = unit_ref
    self.context_ref = context_ref

  def get_key(self):
    return self.key

  def get_value(self):
    return self.value

  def get_decimals(self):
    return self.decimals

  def get_unit_ref(self):
    return self.unit_ref

  def get_context_ref(self):
    return self.context_ref

  @staticmethod
  def create(node):
    key = EdinetDataUtil.get_key(node)
    value = EdinetDataUtil.get_value(node)
    decimals = EdinetDataUtil.get_decimals(node)
    unit_ref = EdinetDataUtil.get_unit_ref(node)
    context_ref = EdinetDataUtil.get_context_ref(node)
    return EdinetData(key, value, decimals, unit_ref, context_ref)


class EdinetXbrlObject(object):
  def __init__(self):
    self._data_dict = OrderedDict()

  def clear(self):
    self._data_dict.clear()

  def put(self, key, edinet_data):
    if self.has_key(key):
      self._data_dict[key].append(edinet_data)
    else:
      self._data_dict[key] = [edinet_data]

  def get_data_list(self, key, auto_lower=True):
    if auto_lower:
      key = key.lower()

    return self._data_dict.get(key, [])

  def get_data_by_context_ref(self, key, context_ref):
    val = list(filter(lambda d: d.get_context_ref() == context_ref, self.get_data_list(key)))
    if val:
      return val[0]
    else:
      return None

  def get_keys(self):
    return self._data_dict.keys()

  def has_key(self, key):
    return (key in self._data_dict)
