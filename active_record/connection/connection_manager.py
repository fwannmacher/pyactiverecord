"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import utilities.design_pattern.singleton
from i_connector import IConnector

class ConnectionManager(utilities.design_pattern.singleton.Singleton):
	def __init__(self):
		self._connector = None

	@property
	def connector(self):
		return self._connector

	@connector.setter
	def connector(self, connector):
		if not isinstance(connector, IConnector):
			raise TypeError("connector must be a subclass of active_record.connection.IConnector")

		self._connector = connector