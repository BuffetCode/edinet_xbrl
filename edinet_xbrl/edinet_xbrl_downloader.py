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

from edinet_xbrl.ufocatcher_util import UfoCatcherUtil
from time import sleep
import urllib.request


class EdinetXbrlDownloader(object):
  @staticmethod
  def download(url, target_dir):
    file_name = "{0}/{1}".format(target_dir, url.split("/")[-1])
    urllib.request.urlretrieve(url, file_name)

  @classmethod
  def download_by_ticker(cls, ticker, target_dir, wait_sec=1.0):
    response = UfoCatcherUtil.request(ticker)
    for url in UfoCatcherUtil.generate_edinet_xbrl_url(response.text):
      cls.download(url, target_dir)
      sleep(wait_sec)
