import unittest
from Crowdmap import Crowdmap

class FindProjTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap= Crowdmap(["I met Or A. at Chabad house Bangkok","We found Or A. R.I.P at Langtang valley","Missing Cowboy"])
								 
	def test_get_all_posts_for_name(self):
		posts= self.crowdmap.get_all_posts_for("Or A.")
		self.assertEquals(["I met Or A. at Chabad house Bangkok","We found Or A. R.I.P at Langtang valley"],posts)

	
	def test_get_all_posts_for_missing_name(self):
		posts = self.crowdmap.get_all_posts_for("Joe")
		self.assertEquals([],posts)
		
	def test_check_if_location_in_post(self):
		location_exist=self.crowdmap.is_location_for_name("Or")
 		self.assertTrue(location_exist)
		
	def test_check_if_diff_location_in_post(self):
		location_exist=self.crowdmap.is_diff_location_for_name("Or")
 		self.assertTrue(location_exist)

if __name__ == '__main__':
	unittest.main()

