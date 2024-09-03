import pandas as pd 
import datatable as dt

def read_large_csv(file_path,chunksize=1000):
    chunked_df=pd.read_csv(file_path,chunksize=chunksize)
    
    df=pd.concat(chunked_df,ignore_index=True)
    print(type(df))
    dtoutput=dt.Frame(df)
    print(type(dtoutput))
    return df


file_path_csv = r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\Basic\FSI-2023-DOWNLOAD.csv"
file_path_csv=r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\Basic\LargeExcel.csv"

data_table = read_large_csv(file_path_csv)

print(data_table)