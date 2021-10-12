#General Imports
from unittest import TestCase
from read_excel import ReadExcel
from lib.exception_handling import FileDoesNotExists, SheetNotFound, WrongFileType



class TestReadExcel(TestCase):

  def setUp(self) -> None:
      self.wrong_file_location = './data.xls'
      self.good_file_location = '../test_assets/data.xls'
      self.bad_file_extension = '../test_assets/data.xld'

  def test_wrong_location(self):
    """Error Handler"""
    with self.assertRaises(FileDoesNotExists):
      ReadExcel(self.wrong_file_location)

  def test_good_location(self):
    """Success Handler"""
    ReadExcel(self.good_file_location)

  def test_bad_file_extension(self):
    """Error Handler"""
    with self.assertRaises(WrongFileType):
      ReadExcel(self.bad_file_extension)

  def test_read_range_of_rows(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    rows = excel_data.read_range_of_rows(1,10)
    self.assertEqual(len(rows), 9)

  def test_number_of_rows(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    number = excel_data.number_of_rows
    self.assertEqual(number, 10)

  def test_read_row(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    row = excel_data.read_row(1)
    existing_row = [1.0, 'Dulce', 'Abril', 'Female', 'United States', 32.0, '15/10/2017', 1562.0]
    self.assertEqual(row, existing_row)


  def test_number_of_columns(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    number = excel_data.number_of_columns
    self.assertEqual(number, 8)


  def test_columns_header_names(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    names = excel_data.columns_header_names
    existing_names = [0, 'First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id']
    self.assertEqual(names, existing_names)


  def test_read_column(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    col = excel_data.read_column(0)
    existing_col = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.assertEqual(col, existing_col)


  def test_get_cell_value(self):
    """Success Handler"""    
    excel_data = ReadExcel(self.good_file_location)
    cell = excel_data.get_cell_value(0,0)
    self.assertEqual(cell, 0)
