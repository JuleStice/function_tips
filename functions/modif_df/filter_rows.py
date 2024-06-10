
# Function to remove duplicates from the entire DataFrame
# Input: 
#   - dataframe: The DataFrame from which duplicates need to be removed
# Output: 
#   - df_without_duplicates: The DataFrame with duplicates removed
def duplicates_dropped(dataframe):
    df_without_duplicates = dataframe.drop_duplicates()
    return df_without_duplicates

# Function to remove duplicates based on a specific column
# Input: 
#   - dataframe: The DataFrame from which duplicates need to be removed
#   - column: The column based on which duplicates should be identified
#   - keep: Determines which duplicates (if any) to keep. 'first', 'last', or False
# Output: 
#   - df_without_duplicates: The DataFrame with duplicates removed based on the specified column
def duplicates_dropped_by_column(dataframe, column, keep):
    df_without_duplicates = dataframe.drop_duplicates(subset=[column], keep=keep)
    return df_without_duplicates

# Function to remove rows containing null values from the entire DataFrame
# Input: 
#   - dataframe: The DataFrame from which rows with null values need to be removed
# Output: 
#   - df_without_null_values: The DataFrame with rows containing null values removed
def drop_is_null_values(dataframe):
    df_without_null_values = dataframe.dropna()
    return df_without_null_values

# Function to remove rows containing null values in specific columns
# Input: 
#   - dataframe: The DataFrame from which rows with null values need to be removed
#   - list_columns: List of columns to check for null values
# Output: 
#   - df_without_null_values: The DataFrame with rows containing null values in specified columns removed
def drop_is_null_values_in_columns(dataframe, list_columns):
    df_without_null_values = dataframe.dropna(subset=list_columns)
    return df_without_null_values









