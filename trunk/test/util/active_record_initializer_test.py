"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import unittest
from test import mock
import active_record.connection
active_record.connection.ConnectionManager.instance.connector = mock.DummyConnector()
import active_record.util

class ActiveRecordInitializerTestCase(unittest.TestCase):
	def test_initialize(self):
		active_record.util.ActiveRecordInitializer.initialize(mock.DummyClass, "dummy_classes")

		self.assertEqual(mock.DummyClass.table_name, "dummy_classes")

		dummy_object = mock.DummyClass()

		self.assertTrue(hasattr(dummy_object, "integer"))
