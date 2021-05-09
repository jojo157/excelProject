from openpyxl import load_workbook
import json


workbook = load_workbook(filename="testDict.xlsx")
sheet = workbook.active

dict_value = sheet["C1"].value 
# using json.loads()
# convert dictionary string to dictionary
dict_value = json.loads(dict_value)

print(dict_value["key1"])
