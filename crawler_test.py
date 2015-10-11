import unittest
from crawler import crawler
import os
import sys

class CrawlerTest(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_unique_word_count(self):
		"""Compare count of unique words from test web 
		pages to the length of the inverted index (which 
		should be a	count of unique words)"""

		self.assertEqual(len(bot.get_inverted_index()), 11)

	def test_unique_word_in_page(self):
		"""Check for the unique word in each respective 
		page (one word per page)"""
		# Test Unique Word In Page
		tuwip = bot.get_resolved_inverted_index()
		self.assertEqual(tuwip["uniquezero"], set(["http://localhost:8080/test0"]))
		self.assertEqual(tuwip["uniqueone"], set(["http://localhost:8080/test1"]))
		self.assertEqual(tuwip["uniquetwo"], set(["http://localhost:8080/test2"]))
		self.assertEqual(tuwip["uniquethree"], set(["http://localhost:8080/test3"]))

	def test_common_word(self):
		"""Check that the common word, 'test', appeared
		in each page"""
		# Test Common Word
		tcw = bot.get_resolved_inverted_index()
		self.assertEqual(tcw["test"], set(["http://localhost:8080/test3", "http://localhost:8080/test2", "http://localhost:8080/test1", "http://localhost:8080/test0"]))

	def test_shared_words(self):
		"""Check for specific words shared between specific
		pages. E.g. 'onetwo' is shared between page 1 & 2"""
		# Test Shared Word
		tsw = bot.get_resolved_inverted_index()
		self.assertEqual(tsw["zeroone"], set(["http://localhost:8080/test1", "http://localhost:8080/test0"]))
		self.assertEqual(tsw["zerotwo"], set(["http://localhost:8080/test2", "http://localhost:8080/test0"]))
		self.assertEqual(tsw["zerothree"], set(["http://localhost:8080/test3", "http://localhost:8080/test0"]))
		self.assertEqual(tsw["onetwo"], set(["http://localhost:8080/test2", "http://localhost:8080/test1"]))
		self.assertEqual(tsw["onethree"], set(["http://localhost:8080/test3", "http://localhost:8080/test1"]))
		self.assertEqual(tsw["twothree"], set(["http://localhost:8080/test3", "http://localhost:8080/test2"]))



if __name__ == '__main__':
	bot = crawler(None, "urls.txt")
	bot.crawl(depth=1)
	unittest.main()
