import pandas as pd

# Dosyanın yolunu belirtelim
file_path = "/Users/onuruca/Desktop/eedi meü denizcilik/Analiz/CONTAINER/container.xlsx"

# Dosyanın ilk birkaç satırını okuyarak değişkenleri (sütun adlarını) belirleyelim
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

# Tüm sayfalardaki değişkenleri (sütun isimlerini) listeleyelim
variables = {sheet: pd.read_excel(xls, sheet_name=sheet).columns.tolist() for sheet in sheet_names}
variables
print(variables)