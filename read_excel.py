import xlrd
from xlrd.book import Book
from xlrd.sheet import Sheet
from lib.exception_handling import FileDoesNotExists, SheetNotFound


class ReadExcel: 

  def __init__(self, path: str , sheet_index: int = 0) -> None:
    # Config
    self.__sheet_index = sheet_index
    self.__workbook = self.read_workbook(path)
    self.__sheet = self.read_sheet(self.__workbook)

    # Rows
    self.number_of_rows = self.__sheet.nrows
    self.read_row = lambda index: self.__sheet.row_values(index)
    
    # Columns
    self.number_of_columns = self.__sheet.ncols
    self.columns_header_names = [self.__sheet.cell_value(0, i) for i in range(self.number_of_columns)]
    self.read_column = lambda index: self.__sheet.col_values(index)

    # Utilities
    self.get_cell_value = lambda row, col: self.__sheet.cell_value(row, col)

  def read_workbook(self, path: str) -> Book:
    try:
      return xlrd.open_workbook(path)
    except FileNotFoundError:
      raise FileDoesNotExists

  def read_sheet(self, workbook: Book) -> Sheet:
    try:
      return workbook.sheet_by_index(self.__sheet_index)
    except IndexError:
      raise SheetNotFound

  def read_range_of_rows(self, start: int, end: int) -> list:
    rows: list = []
    for row in range(start, end):
      new_row = [self.__sheet.cell_value(row, i) for i in range(self.number_of_columns)]
      rows.append(new_row)
    return rows
