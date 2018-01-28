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

import xml.etree.ElementTree as ET
import requests


class UfoCatcherUtil(object):
  NAMESPACE = '{http://www.w3.org/2005/Atom}'
  FAKE_HTTP_HEADER = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36))"}
  UFOCATCH_URL = 'http://resource.ufocatch.com/atom/edinetx/query'

  @classmethod
  def create_url(cls, query):
    return "{0}/{1}".format(cls.UFOCATCH_URL, query)

  @classmethod
  def request(cls, tikcer, headers=FAKE_HTTP_HEADER):
    return requests.get(url=cls.create_url(tikcer), headers=headers)

  @classmethod
  def is_edinet_xbrl_url(cls, element):
    url = cls.get_href_attrib(element)
    return False if url is None else ("PublicDoc" in url and url.endswith(".xbrl"))

  @classmethod
  def get_et_tree(cls, html):
    et_tree = ET.fromstring(html)
    ET.register_namespace('', cls.NAMESPACE[1:-1])
    return et_tree

  @classmethod
  def generate_edinet_xbrl_url(cls, html):
    et_tree = cls.get_et_tree(html)
    for el in et_tree.findall('.//' + cls.NAMESPACE + 'entry'):
      for link in el.findall('./' + cls.NAMESPACE +'link[@type="text/xml"]'):
        if cls.is_edinet_xbrl_url(link):
          yield cls.get_href_attrib(link)

  @staticmethod
  def get_href_attrib(element):
    return element.attrib.get('href', None)
