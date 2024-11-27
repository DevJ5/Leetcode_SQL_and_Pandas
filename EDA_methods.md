1. head():

   Returns the first 5 rows by default (you can specify a different number).
   Great for quickly previewing the data.

df.head() # First 5 rows (default)
df.head(10) # First 10 rows

2. tail():

   Returns the last 5 rows by default (you can specify a different number).
   Useful for inspecting the end of the DataFrame.

df.tail() # Last 5 rows (default)
df.tail(10) # Last 10 rows

3. shape:

   Returns a tuple representing the dimensions of the DataFrame: (number of rows, number of columns).
   Useful for checking the size of the DataFrame.

df.shape # (rows, columns)

4. info():

   Provides a summary of the DataFrame including the number of non-null entries, column types, and memory usage.
   Helps to understand the data types of each column and the presence of any missing values.

df.info()

5. describe():

   Returns a summary statistics of the DataFrame, such as count, mean, std deviation, min, max, and quartiles for numeric columns.
   Great for getting an overview of the distribution of numeric data.

df.describe()

6. columns:

   Returns a list of column names in the DataFrame.
   Useful for understanding what features/variables are present in the data.

df.columns # List of column names

7. dtypes:

   Returns the data types of each column in the DataFrame.
   Useful for checking if columns are in the expected formats (e.g., numeric, string, datetime).

df.dtypes # Data types of each column

8. value_counts():

   For categorical columns, it returns the count of unique values in that column.
   Great for understanding the distribution of values, especially in categorical data.

df['column_name'].value_counts()

9. isnull() / sum():

   isnull() checks for missing values and returns a DataFrame of booleans.
   sum() on top of isnull() gives the count of missing values for each column.

df.isnull().sum() # Count of missing values in each column

10. sample():

    Returns a random sample of rows from the DataFrame.
    Useful for quickly checking the data when you have a large dataset.

df.sample(5) # Random sample of 5 rows

11. unique():

    Returns the unique values in a column (useful for categorical or string columns).

df['column_name'].unique() # Unique values in a column

12. nunique():

    Returns the number of unique values in each column.

df.nunique() # Number of unique values in each column

13. corr():

    Computes the correlation matrix of numeric columns.
    Helps to understand relationships between numeric variables.

df.corr() # Correlation matrix of numeric columns

14. import seaborn as sns
    sns.histplot(df['some_column']) # Histogram for a column
    sns.scatterplot(x='col1', y='col2', data=df) # Scatter plot for relationships
