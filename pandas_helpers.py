'''Functions for converting values, grouping, etc. to a pandas dataframes'''

def convert_date_time(df, column, new_column_name, days):
    '''converts values in a  column into a datatime and returns array of values
    that that are greater # of days provided'''
    df[column] = pd.to_datetime(df[column])
    df[new_column_name] = (df[column].max() - df[column])  > dtm.timedelta(days)
    return(df)
