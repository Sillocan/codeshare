import pandas as pd
import sys

def read_from_excel(path, sheetname):
    with open(path,'rb') as file:
        return pd.read_excel(file, sheetname=sheetname)
    
# Hardcoding paths for convinence
file1 = sys.argv[1]
sheet1 = sys.argv[2]

file2 = sys.argv[3]
sheet2 = sys.argv[4]

column_name = "Part Number"

print(f"Merging '{column_name}' from {file1}:{sheet1} with {file2}:{sheet2}")
    
# Read them
dataframe1 = read_from_excel(file1, sheet1)
dataframe2 = read_from_excel(file2, sheet2)

# Merge the two together
merged_dataframe = pd.merge(dataframe1, dataframe2, on=column_name, how='right')

# Output the files - overwriting the second sheet
with pd.ExcelWriter(file2, if_sheet_exists='replace') as writer:
    merged_dataframe.to_excel(writer, sheet_name=sheet2, index=False)
```

Or, if you want to overwrite a single sheet:

```python
# Output the files - overwriting the second sheet
with pd.ExcelWriter(file2, if_sheet_exists='replace') as writer:
    merged_dataframe.to_excel(writer, sheet_name=sheet2, index=False)
    
