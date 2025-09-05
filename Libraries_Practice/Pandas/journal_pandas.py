
import numpy as np
import pandas as pd

dict69 = {
  "Names": ["Akash", "Moiz", "Mueed", "Mueed"],
  "Marks": [89, 99, 69, 92],
  "City": ["Delhi", "Karachi", "Hyderabad", "liaquatabad"]

}
# data1 = pd.DataFrame(dict69)
excel_data = pd.read_excel("Students.xlsx", sheet_name="EMPLOYEE_DATA")
excel_data.loc[1, "NAME OF EMPLOYEE"] = "Junaid bangali"
excel_data.to_excel("Students.xlsx", sheet_name="EMPLOYEE_DATA")
