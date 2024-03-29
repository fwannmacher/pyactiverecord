"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import unittest
import active_record.relation

class QueryTestCase(unittest.TestCase):
	def test_distinct(self):
		dummy_query = active_record.relation.Query()
		dummy_query.distinct()

		self.assertTrue(dummy_query.context[active_record.relation.Context.Scopes.DISTINCT])

		dummy_query.distinct(False)

		self.assertFalse(dummy_query.context[active_record.relation.Context.Scopes.DISTINCT])

	def test_from_table(self):
		dummy_query = active_record.relation.Query()
		dummy_query.from_table("some")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.FROM], "some")

		dummy_query.from_table("another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.FROM], "another")

	def test_group(self):
		dummy_query = active_record.relation.Query()
		dummy_query.group("some, another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.GROUP], "some, another")

		dummy_query.group(["third", "fourth"])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.GROUP], "some, another,third,fourth")

		success = False

		try:
			dummy_query.group(1)
		except TypeError:
			success = True

		self.assertTrue(success)

	def test_having(self):
		dummy_query = active_record.relation.Query()
		dummy_query.having("some and ?", "another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.HAVING], "some and another")

	def test_includes(self):
		dummy_query = active_record.relation.Query()
		dummy_query.includes("some", "another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.INCLUDES], ["some", "another"])

		dummy_query.unescope(active_record.relation.Context.Scopes.INCLUDES)
		dummy_query.includes(["some", "another"])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.INCLUDES], ["some", "another"])

		dummy_query.unescope(active_record.relation.Context.Scopes.INCLUDES)
		dummy_query.includes({"some" : "another"})

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.INCLUDES][0], {"some" : "another"})

		success = False

		try:
			dummy_query.includes(1)
		except TypeError:
			success = True

		self.assertTrue(success)

	def test_joins(self):
		dummy_query = active_record.relation.Query()
		dummy_query.joins("some", "another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.JOINS], ["some", "another"])

		dummy_query.unescope(active_record.relation.Context.Scopes.JOINS)
		dummy_query.joins(["some", "another"])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.JOINS], ["some", "another"])

		dummy_query.unescope(active_record.relation.Context.Scopes.JOINS)
		dummy_query.joins({"some" : "another"})

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.JOINS][0], {"some" : "another"})

		success = False

		try:
			dummy_query.joins(1)
		except TypeError:
			success = True

		self.assertTrue(success)

	def test_limit(self):
		dummy_query = active_record.relation.Query()
		dummy_query.limit(1)

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.LIMIT], 1)

	def test_offset(self):
		dummy_query = active_record.relation.Query()
		dummy_query.offset(1)

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.OFFSET], 1)

	def test_order(self):
		dummy_query = active_record.relation.Query()
		dummy_query.order("some DESC, another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some DESC,another ASC")

		dummy_query.unescope(active_record.relation.Context.Scopes.ORDER)
		dummy_query.order("some", "another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some ASC,another ASC")

		dummy_query.unescope(active_record.relation.Context.Scopes.ORDER)
		dummy_query.order(["some", "another"])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some ASC,another ASC")

		dummy_query.unescope(active_record.relation.Context.Scopes.ORDER)
		dummy_query.order({"some" : "DESC", "another" : "ASC"})

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some DESC,another ASC")

		dummy_query.unescope(active_record.relation.Context.Scopes.ORDER)
		dummy_query.order("some", {"another" : "DESC"})

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some ASC,another DESC")

		dummy_query.unescope(active_record.relation.Context.Scopes.ORDER)
		dummy_query.order(some="ASC", another="DESC")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some ASC,another DESC")

		success = False

		try:
			dummy_query.order(None)
		except TypeError:
			success = True

		self.assertTrue(success)

	def test_preload(self):
		dummy_query = active_record.relation.Query()
		dummy_query.preload("some")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.INCLUDES], ["some"])

	def test_reorder(self):
		dummy_query = active_record.relation.Query()
		dummy_query.order("some")
		dummy_query.reorder("another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "another ASC")

	def test_reverse_order(self):
		dummy_query = active_record.relation.Query()
		dummy_query.order("some AsC, another dESC, third asc, fourth deSC")
		dummy_query.reverse_order()

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.ORDER], "some DESC,another ASC,third DESC,fourth ASC")

	def test_select(self):
		dummy_query = active_record.relation.Query()
		dummy_query.select("some", "another")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.SELECT], "some,another")

		dummy_query.select("some")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.SELECT], "some")

	def test_uniq(self):
		dummy_query = active_record.relation.Query()
		dummy_query.uniq()

		self.assertTrue(dummy_query.context[active_record.relation.Context.Scopes.DISTINCT])

		dummy_query.uniq(False)

		self.assertFalse(dummy_query.context[active_record.relation.Context.Scopes.DISTINCT])
		
	def test_where(self):
		dummy_query = active_record.relation.Query()
		dummy_query.where("test")

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "test")

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where("? ? ?", "a", 1, ['b', 2])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "'a' 1 ('b',2)")

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where([":a :b", {"a" : "a", "b" : 1}])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "'a' 1")

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where(["'%s' %d", "a", 1])

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "'a' 1")

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where({"a" : "a", "b" : [1]})

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "a = 'a' AND b IN (1)")

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where("test")
		dummy_query.where("test")

		self.assertEqual(len(dummy_query.context[active_record.relation.Context.Scopes.WHERE]), 2)

		dummy_query.unescope(active_record.relation.Context.Scopes.WHERE)
		dummy_query.where(a="a", b=1)

		self.assertEqual(dummy_query.context[active_record.relation.Context.Scopes.WHERE][0], "a = 'a' AND b = 1")

		success = False

		try:
			dummy_query.where(True)
		except TypeError:
			success = True

		self.assertTrue(success)
