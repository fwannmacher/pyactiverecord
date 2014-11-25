"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import utilities.design_pattern.singleton
import utilities.string

class ActiveRecordHolder(utilities.design_pattern.singleton.Singleton):
	def __init__(self):
		self._active_records = {}

	def add_active_record(self, active_record):
		self._active_records[utilities.string.CaseConverter.convert_to_snake_case(active_record.__name__)] = active_record
		self._active_records[active_record.table_name] = active_record

	def get_active_record_by_table_name(self, table_name):
		return self._active_records[table_name] if table_name in self._active_records else None

	def get_active_record_by_name(self, name):
		name = utilities.string.CaseConverter.convert_to_snake_case(name)

		return self._active_records[name] if name in self._active_records else None