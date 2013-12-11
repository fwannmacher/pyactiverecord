"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

class PropertyAttacher:
	@staticmethod
	def attach_property(cls, property_name, property_type = None):
		"""
		Attaches a new property, named <property_name>, to the class <cls>
		"""
		attribute = "_" + property_name

		def get_attribute_value(self):
			return getattr(self, attribute, None)

		def set_attribute_value(self, property_value):
			setattr(self, attribute, property_value)

		def type_safe_set_attribute_value(self, property_value):
			if type(property_value) is not property_type:
				raise TypeError("Wrong value type for {0}. Expected {1}, got {2}.".format(property_name, property_type, type(property_value)))

			setattr(self, attribute, property_value)

		def del_attribute_value(self):
			delattr(self, attribute)

		setattr(cls, property_name, property(get_attribute_value, set_attribute_value if property_type is None else type_safe_set_attribute_value, del_attribute_value))