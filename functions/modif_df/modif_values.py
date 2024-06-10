
def replace_values(dataframe,value_replaced,value_to_replace):
    df_replaced_values = dataframe.replace(value_replaced,value_to_replace)
    return df_replaced_values

    
def replace_values_only_column(dataframe,column_name,value_replaced,value_to_replace):
    df_replaced_values = dataframe[column_name].replace(value_replaced,value_to_replace)
    return df_replaced_values