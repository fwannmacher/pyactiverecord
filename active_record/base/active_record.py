"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

from active_record_metaclass import ActiveRecordMetaclass

class ActiveRecord(object):
	__metaclass__ = ActiveRecordMetaclass

	@classmethod
	def find(cls, value, primary_key = "id"):
		return None
