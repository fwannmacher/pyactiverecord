"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import unittest
import active_record

class ClassPropertyCase(unittest.TestCase):
	def test_class_property(self):
		class DummyClass:
			@active_record.decorator.class_property
			@classmethod
			def dummy_property(cls):
				return cls

		self.assertEqual(DummyClass.dummy_property, DummyClass)
