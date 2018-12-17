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


import unittest
from xml.etree.ElementTree import Element
from nose.tools import eq_, assert_true, assert_false
from edinet_xbrl.ufocatcher_util import UfoCatcherUtil


class UfoCatcherUtilTest(unittest.TestCase):
    @staticmethod
    def test_create_url():
        query = 'aaa'
        eq_('http://resource.ufocatch.com/atom/edinetx/query/' + query, UfoCatcherUtil.create_url(query))

    @staticmethod
    def test_is_edinet_xbrl_url():
        # true
        ok_element = Element("", {"href": "http://aaa.bbb/PublicDoc/ccc.xbrl"})
        assert_true(UfoCatcherUtil.is_edinet_xbrl_url(ok_element))

        # false
        for ng_element in [Element("", {"href": "http://aaa.bbb/ccc.xbrl"}),
                           Element("", {"href": "http://aaa.bbb/PublicDoc/ccc.html"})]:
            assert_false(UfoCatcherUtil.is_edinet_xbrl_url(ng_element))

    @staticmethod
    def test_get_href_attrib():
        href = "http://aaa.bbb/PublicDoc/ccc.xbrl"
        element = Element("", {"href": href})
        eq_(href, UfoCatcherUtil.get_href_attrib(element))
        # if href attrib is unset
        eq_(None, UfoCatcherUtil.get_href_attrib(Element("")))


if __name__ == '__main__':
    unittest.main()
