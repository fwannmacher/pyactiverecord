"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import abc
import utilities.string
from .. import interface
from .. import util

class ActiveRecordMetaclass(abc.ABCMeta):
	def __init__(cls, name, bases, dct):
		abc.ABCMeta.__init__(cls, name, bases, dct)

		tokens = utilities.string.CaseConverter.convert_to_snake_case(name).rsplit("_", 1)
		last_token = tokens[-1]
		left_tokens = tokens[-2] + "_" if len(tokens) > 1 else ""
		table_name = left_tokens + utilities.string.Pluralizer.pluralize(last_token)

		util.ActiveRecordInitializer.initialize(cls, table_name)

class ActiveRecord(interface.IActiveRecord):
	__metaclass__ = ActiveRecordMetaclass
