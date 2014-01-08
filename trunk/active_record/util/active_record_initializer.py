"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import utilities.reflection.util
from .. import connection
from .. import interface

class ActiveRecordInitializer:
	@staticmethod
	def initialize(cls, table_name):
		if not issubclass(cls, interface.IActiveRecord):
			raise TypeError("cls must be a subclass of IActiveRecord")

		connector = connection.ConnectionManager.instance.connector

		if connector is not None and connector.table_exists(table_name):
			setattr(cls.__metaclass__, "table_name", property(lambda cls: table_name))

			for column_name, column_type in connector.get_table_columns(table_name):
				utilities.reflection.util.PropertyAttacher.attach_property(cls, column_name, column_type)
