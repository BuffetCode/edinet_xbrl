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


import os
import unittest
from nose.tools import eq_
from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
import yaml
import codecs


class EdinetXbrlParserTestCase(unittest.TestCase):
    TEST_DIR = "{0}/test_data".format(os.path.dirname(os.path.abspath(__file__)))
    EMPLOYEES_NUM_KEY = "jpcrp_cor:NumberOfEmployees"
    ASSETS_NUM_KEY = "jppfs_cor:Assets"
    NETSALES_KEY = "jppfs_cor:NetSales"
    CURRENT_YEAR_INSTANT_CONTEXT = "CurrentYearInstant"
    CURRENT_YEAR_DURATION_CONTEXT = "CurrentYearDuration"
    CURRENT_YEAR_INSTANT_NON_CON_CONTEXT = "CurrentYearInstant_NonConsolidatedMember"
    CURRENT_YEAR_DURATION_NON_CON_CONTEXT = "CurrentYearDuration_NonConsolidatedMember"

    @staticmethod
    def parse(xbrl_file_path):
        parser = EdinetXbrlParser()
        return parser.parse_file(xbrl_file_path)

    @classmethod
    def get_xbrl_file(cls, target):
        return "{0}/{1}.xbrl".format(cls.TEST_DIR, target)

    @classmethod
    def get_expected_dict(cls, target):
        yaml_file = "{0}/{1}.yaml".format(cls.TEST_DIR, target)
        with codecs.open(yaml_file, 'r', 'utf-8') as f:
            return yaml.load(f)

    @classmethod
    def test_kakaku(cls):
        target = "CJ_2371_kakakucom"
        xbrl_file = cls.get_xbrl_file(target)
        data_container = cls.parse(xbrl_file)
        expected_dict = cls.get_expected_dict(target)
        eq_(expected_dict["employees_num"],
            int(data_container.get_data_by_context_ref(cls.EMPLOYEES_NUM_KEY,
                                                       cls.CURRENT_YEAR_INSTANT_CONTEXT).get_value()))
        eq_(expected_dict["assets"],
            int(data_container.get_data_by_context_ref(cls.ASSETS_NUM_KEY,
                                                       cls.CURRENT_YEAR_INSTANT_CONTEXT).get_value()))
        eq_(expected_dict["netsales"],
            int(data_container.get_data_by_context_ref(cls.NETSALES_KEY,
                                                       cls.CURRENT_YEAR_DURATION_CONTEXT).get_value()))

    @classmethod
    def test_yahoo(cls):
        target = "CI_4689_yahoo"
        xbrl_file = cls.get_xbrl_file(target)
        data_container = cls.parse(xbrl_file)
        expected_dict = cls.get_expected_dict(target)
        eq_(expected_dict["employees_num"],
            int(data_container.get_data_by_context_ref(cls.EMPLOYEES_NUM_KEY,
                                                       cls.CURRENT_YEAR_INSTANT_NON_CON_CONTEXT).get_value()))
        eq_(expected_dict["assets"],
            int(data_container.get_data_by_context_ref(cls.ASSETS_NUM_KEY,
                                                       cls.CURRENT_YEAR_INSTANT_NON_CON_CONTEXT).get_value()))
        eq_(expected_dict["netsales"],
            int(data_container.get_data_by_context_ref(cls.NETSALES_KEY,
                                                       cls.CURRENT_YEAR_DURATION_NON_CON_CONTEXT).get_value()))


if __name__ == '__main__':
    unittest.main()
