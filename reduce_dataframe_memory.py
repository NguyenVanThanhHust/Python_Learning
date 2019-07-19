"""
link : https://www.kaggle.com/arjanso/reducing-dataframe-memory-size-by-65
main idea : 
- default value in pandas is np.float64
- check if a value can be integer
- check range of that integer, convert to np.uint8 and so on.
"""


import numpy as np
import pandas as pd

def reduce_memory_usage(props):
    start_mem_usg = props.memory_usage().sum() / 1024**2
    print("Memory usage of properties dataframe is: ", str(start_mem_usg), " MB")
    NAlist = [] # keep track of columns that have missing values filled in
    for col in props.columns:
        # Exclude string 
        print("Column: ", col)
        print("dtype before: ", props[col].dtype)
        
        # make variables for Int, max and min
        isInt = False
        mx = props[col].max()
        mn = props[col].min()
        
        # Integer does not support NA, therefore NA needs to be filled
        if not np.isfinite(props[col]).all():
            NAlist.append(col)
            props[col].fillna(mn - 1, inplace = True)
            
        # test if column can be converted to an integer
        asint = props[col].fillna(0).astype(np.int64)
        result = (props[col] -asint)
        result = result.sum()
        if result > -0.1 and result < 0.01:
            isInt = True
            
        # Make Integer/ unsigned integer datatypes
        if isInt:
            if mn > 0:
                if mx < 255:
                    props[col] = props[col].astype(np.uint8)
                elif mx < 65535:
                    props[col] = props[col].astype(np.uint16)
                elif mx < 4294967295:
                    props[col] = props[col].astype(np.uint32)
                else:
                    props[col] = props[col].astype(np.uint64)
            else:
                if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                    props[col] = props[col].astype(np.int8)
                elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                    props[col] = props[col].astype(np.int16)
                elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                    props[col] = props[col].astype(np.int32)
                elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                    props[col] = props[col].astype(np.int16)
        else:
            props[col] = props[col].astype(np.float32)
            
        # Print new column type
        print('dtype after: ', props[col].dtype)
        
    print("Memory usage after completion")
    mem_usg = props.memory_usage().sum() / 1024**2
    print("Memory usage is: ", str(mem_usg), " MB")
    return props, NAlist
    
props = pd.read_csv('./zillow-prize-1/properties_2016.csv')
props, NAlist = reduce_memory_usage(props)