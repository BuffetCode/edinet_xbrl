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
import shutil
import tempfile
import unittest

from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader


class EdinetXbrlDownloaderTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_next_file_name_keeps_extension_separator(self):
        original_file = os.path.join(self.test_dir, "sample.xbrl")
        with open(original_file, "w"):
            pass

        numbered_file = EdinetXbrlDownloader._EdinetXbrlDownloader__get_next_file_name(original_file)

        self.assertEqual(os.path.join(self.test_dir, "sample(1).xbrl"), numbered_file)


if __name__ == '__main__':
    unittest.main()
