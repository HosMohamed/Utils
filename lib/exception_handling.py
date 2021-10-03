class FileDoesNotExists(Exception):
  def __init__(self, message = '') -> None:
      message = 'The file you wish to read does NOT exist in the location you specified.'
      super().__init__(message)

class SheetNotFound(Exception):
  def __init__(self, message = '') -> None:
      message = 'The sheet you wish to read does NOT exist in the index you specified.'
      super().__init__(message)