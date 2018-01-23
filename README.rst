edinet_xbrl
########################################
.. image:: https://badge.fury.io/py/edinet-xbrl.svg
    :target: https://badge.fury.io/py/edinet-xbrl
.. image:: https://travis-ci.org/BuffetCode/edinet_xbrl.svg?branch=master
    :target: https://travis-ci.org/BuffetCode/edinet_xbrl

edinet_xbrl is a Python parser for Edinet xbrl files.


Installation
===============
.. Installation
   ------------

To install edinet_xbrl, simply:


.. code-block:: bash

  $ pip install edinet_xbrl

.. 


How to Use
===============
.. HowToUse
To get value from your xbrl files, easily:

.. code-block:: python

  from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

  ## init parser
  parser = EdinetXbrlParser()

  ## parse xbrl file and get data container
  xbrl_file_path = "set your xbrl file path"
  data_container = parser.parse_file(xbrl_file_path)

  ## get value from container
  key = "jppfs_cor:Assets"
  context_ref = "CurrentYearInstant"
  current_year_assets = data_container.get_rawdata_by_context_ref(key, context_ref).get_value()

..
