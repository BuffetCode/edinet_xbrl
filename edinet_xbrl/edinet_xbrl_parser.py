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

from xbrl import XBRLParser
from edinet_xbrl.rawdata import Rawdata, RawdataContainer
import codecs

class EdinetXbrlParser(object):
  @classmethod
  def parse_file(cls, xbrl_file_path):
    data_container = RawdataContainer()
    with codecs.open(xbrl_file_path, 'r', 'utf-8') as of:
      parser = XBRLParser.parse(of)
      for node in parser.find_all():
        cls.put_node(data_container, node)
    return data_container

  @staticmethod
  def put_node(data_container, node):
    data_container.put_rawdata(node.name, Rawdata.create(node))

