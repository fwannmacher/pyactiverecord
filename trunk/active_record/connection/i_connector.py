"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import abc

class IConnector(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def table_exists(self, table_name):
		"""Verifies if table exists in the database."""

	@abc.abstractmethod
	def get_table_columns(self, table_name):
		"""Gets the table columns from the database."""