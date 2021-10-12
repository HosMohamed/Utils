#General Imports
from json.decoder import JSONDecodeError
from unittest import TestCase
from read_json import ReadJSON


class TestReadJSON(TestCase):

  def setUp(self) -> None:
      self.wrong_file_location = './data.json'
      self.good_file_location = '../test_assets/data.json'
      self.no_data_file_location = '../test_assets/no_data.json'
      self.bad_file_extension = '../test_assets/data.jso'

  def test_wrong_location(self):
    """Error Handler"""
    with self.assertRaises(FileNotFoundError):
      ReadJSON(self.wrong_file_location)

  def test_good_location(self):
    """Success Handler"""
    ReadJSON(self.good_file_location)

  def test_bad_file_extension(self):
    """Error Handler"""
    with self.assertRaises(FileNotFoundError):
      ReadJSON(self.bad_file_extension)

  def test_no_data(self):
    """Error Handler"""    
    with self.assertRaises(Exception):
      ReadJSON(self.no_data_file_location)
