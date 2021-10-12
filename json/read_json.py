import json
from json.decoder import JSONDecodeError


class ReadJSON:
    
    def __init__(self, file_path: str) -> None:
        self.data = self.read(file_path)

    def read(self, path: str):
        try:
            file = open(path)
            data = json.load(file)
            if len(data) > 0:
                return data
        except FileNotFoundError:
            raise FileNotFoundError('File does NOT exist in the path you specified.')
        except JSONDecodeError:
            raise Exception('File was successfully read but it contains no data (Empty)')
        finally:
            file.close()
        
        