"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import active_record.connection

class DummyConnector(active_record.connection.IConnector):
	@property
	def operations(self):
		return active_record.connection.Operations

	def table_exists(self, table_name):
		return True

	def get_table_columns(self, table_name):
		return {"id" : int, "integer" : int}

	def get_table_primary_key(self, table_name):
		return "id"

	def table_record_exists(self, table_name, criteria):
		return True

	def get_table_records(self, table_name, criteria = None, limit = None, order_by = None, columns = None):
		return []

	def execute_table_operation(self, table_name, operation, column):
		return 1
