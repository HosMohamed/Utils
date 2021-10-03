# ReadExcel

## Prerequists:
- Python 3.6 and above.

## File Tree

|-- ReadExcel/.   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- lib/.   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- exception_handling.py   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- .gitignore   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- read_excel.py   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- README.md   
&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;|-- requirements.txt   

## To get started,

- Navigate to the root directory of the repo.
- Install virtualenv `python3 -m pip install virtualenv`.
- Create virtualenv and give it a name. I will be using **env** for this example. `virtualenv env`.
- Activate virtualenv assuming running on macOS or Linus `source  env/bin/activate`.
- Run `python3 -m pip install -r requirements.txt` or `pip3 install -r requirements.txt`.
- Instanciate a new class and pass it the path and the index of the sheet you wish to read e.g 
```javascript
data = ReadExce;('./data.xls', 0)
```
- Get a 2D list of a rows in a certain range and print them
```javascript
rows = excel_data.read_range_of_rows(0, 10)
print(rows)
```
## Features

| Methods | Call Signature |
| ------ | ------ |
| `read_workbook` | (**self**: class instance, **path**: str) => **Book** |
| `read_sheet` | (**self**: class instance, **workbook**: str) => **Sheet** |
| `read_range_of_rows` | (**self**: class instance, **start**: int, **end**: int) => **list(...list<str>)** |
| `number_of_rows` | () => **int** |
| `read_row` | (**index**: int) => **list<str>** |
| `number_of_columns` | () => **int** |
| `columns_header_names`| () => **list<str>** |
| `read_column`| (**index**: int) => **list<str>** |
| `get_cell_value`| (**row**: int, **col**: int) => **str** |

## Contribute

_All contibutions are welcome as long as we are keeping it simple for users._

_Hossam Mohamed_
