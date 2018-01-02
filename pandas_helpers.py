'''Functions for converting values, grouping, etc. to a pandas dataframes'''
import datatime as dt

def time_delta(df, column, new_column_name, days, max):
    '''converts values in a  column into a datatime and returns array of values
    that that are greater than the # of days provided'''
    df[column] = pd.to_datetime(df[column])
    df[new_column_name] = (df[column].max() - df[column])  > dtm.timedelta(days)

    return(df)

def convert_to_mean_except_one(df,column):

'''converts all features to mean except the column listed to NOT convert.
   This is to have compare one feature at a time when all values from other features are held constant.'''

    return(df.loc[:, df.columns != column].apply(np.mean, axis=0, broadcast=True))

'''assign column names to dataframe:'''
df.columns = ['mpg', 'cylinders','displacement','horsepower','weight','acceleration','model_year', 'origin']

'''convert values to floats in dataframe'''
float_df = old_df.convert_objects(convert_numeric=True)
