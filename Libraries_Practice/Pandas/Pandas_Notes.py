
                                # NOTES FOR PANDAS LIBARY!!

# data1 = pd.DataFrame(dict69) # The dataframe class is use to represent data in rows and columns.
# data1.to_csv("friends_data.csv") The to_csv attribute is use to convert the output of our code into excel or csv file.
# data1.to_csv("friendswithnoindexes.csv", index=False) # The index parameter is use to neglect or to insert indexes
# print(data1.head(2)) # .head shows the first elements given in the argument
# print(data1.tail(2)) # .tail shows the last elements given in the argument
# print(data1.describe()) # .describe shows the description of a numeric values(standard deviation, min, max,....)
# pd.read_csv("Train_data.csv") # .read_csv simply outputs the respective csv file on terminal.
# print(spec_data["Marks"]) # We can use square braces to output specific columns
# data1.index = [i+1 for i in range(len(dict69.get("Names")))] # We can use .index to change the values of indexes
# print(data1["Names"][3]) # We can use data1["column_name"]["row index"] to output a specific cell content.
# np.random.rand() # By using this function you can output one or more dimensional arrays.
# data1 = pd.Series() # The series class is use to represent data in a single row.
# data1.dtypes # .dtypes attribute is use to output the data types.
# print(data1.index) # Shows the number of indexes present in a dataframe.
# print(data1.columns) # Shows the number of columns present in a dataframe.
# print(data1.to_numpy()) # convert the respective dataframe into numpy arrays.
# print(data1.sort_index(axis=0, ascending=False)) # It's sort the index into ascending or descending order.
# data2 = data1.copy() # .copy is used to simply copy a dataframe or series.
# data1.loc[1,0] = "Karachi" # .loc function is used to modify or add a new value by giving the location of the cell
# data1.drop('ran', axis=1) # .drop function is used to to delete a column or row
# data1.loc[['A', 'C'], ['Gender', 'Field']] By using .loc we can also obtain specific rows and columns.
# data1.loc[(data1['Names'] > 0.3)] # We can also give a condition in the .loc function.
# data1.iloc[[0, 4], [1, 2]] # .iloc is similar to .loc the only difference is we have pass indexes as arguments
# data1.drop(["A"], axis=0) # If we want to drop or delete a row then we will use this function.
# data1.drop(["Names"], axis=1) # If we want to drop or delete a column then we will use this function.
# data1.drop(["Names", "Age"], axis=1, inplace=True) # If we want to delete the data permanently then use the 'inplace'.
# data1.reset_index() # If we want to reset index numbers then this command we come in handy this will add an additional index column
# data1.reset_index(drop=True) # If we want to reset then this command we come in handy and this will neglect the addtional index column
# data1['Names'].isnull() # You can use the isnull function to see whether a column has null values or not.
# data1.loc[("A", "Names")] = None # By using this command we can make cell null.
# data1.drop_duplicates(subset=['Names']) # You can use this function to delete duplicates in a column
# data1.drop_duplicates(subset=['Names'],keep="last") # The keep attribute is used to choose between first and last.
# data1.drop_duplicates(subset=['Names'],keep=False) # if keep is False then it will duplicates as well as the remaining value
# print(data1.shape) # Outputs the number of rows and columns present in the dataframe.
# print(data1.info()) # It gives detail information of the dataframe
# print(data1['Names'].value_counts()) # Simply count that how many times a value is repeated in a dataframe.
# excel_data = pd.read_excel("Students.xlsx") This command is used to read excel files.
# pd.read_excel("Students.xlsx", sheet_name="EMPLOYEE_DATA") # You can also give specific sheet names as arguments to read it.
