"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import active_record.connection

class DummyConnector(active_record.connection.IConnector):
	def get_table_columns(self, table_name):
		return [("integer", int)]
