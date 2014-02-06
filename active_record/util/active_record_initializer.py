"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import utilities.reflection.util
from .. import connection
import active_record.base

class ActiveRecordInitializer:
	@staticmethod
	def initialize(cls, table_name):
		if not issubclass(cls, active_record.base.ActiveRecord):
			raise TypeError("cls must be a subclass of active_record.base.ActiveRecord")

		connector = connection.ConnectionManager.instance.connector

		if connector.table_exists(table_name):
			setattr(cls.__metaclass__, "primary_key", property(lambda cls: connector.get_table_primary_key(table_name)))
			setattr(cls.__metaclass__, "table_name", property(lambda cls: table_name))

			for column_name, column_type in connector.get_table_columns(table_name).items():
				utilities.reflection.util.PropertyAttacher.attach_property(cls, column_name, column_type)
