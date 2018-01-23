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


class EdinetDataUtil(object):
  CONTEXT_REF = "contextref"
  UNIT_REF = "unitref"
  DECIMALS = "decimals" 
  FORMAT = "format"
  NAME = "name"
  SCALE = "scale"

  @staticmethod
  def get_key(node):
    return node.name

  @staticmethod
  def get_value(node):
    return node.string

  @staticmethod
  def offset(num, power):
    return num * pow(10, power)

  @staticmethod
  def _get_ref_str_value(node, key):
    return node.attrs.get(key, "")

  @staticmethod
  def _get_ref_int_value(node, key):
    return int(node.attrs.get(key, 0))

  @classmethod
  def get_context_ref(cls, node):
    return cls._get_ref_str_value(node, cls.CONTEXT_REF)

  @classmethod
  def get_unit_ref(cls, node):
    return cls._get_ref_str_value(node, cls.UNIT_REF)

  @classmethod
  def get_decimals(cls, node):
    return cls._get_ref_int_value(node, cls.DECIMALS)

  @classmethod
  def get_format(cls, node):
    return cls._get_ref_str_value(node, cls.FORMAT)

  @classmethod
  def get_name(cls, node):
    return cls._get_ref_str_value(node, cls.NAME)

  @classmethod
  def get_scale(cls, node):
    return cls._get_ref_int_value(node, cls.SCALE)
