def cleanAndProcessEnergyData(infile, outfile):
    
    import pandas as pd
    import numpy as np
    
    from numpy import NaN
    
    xdf = pd.read_csv(infile, header = None, low_memory=False)
    
    # Filter out the time-of-use customers.
    
    xdf = xdf[xdf[1]=='Std']
    
    # Replace any string "Null" values with NaN, so that dropna will
    # remove the affected lines.
    
    xdf.replace(["Null"],value = NaN, inplace = True)
    
    # Any blanks or NaN values ?
    
    xdf.dropna(inplace=True)
  
    # Remove any duplicates, using columns 0 through 3 for the identification of
    # duplicates.
    
    xdf.drop_duplicates([0, 1, 2, 3], inplace = True, keep = 'last')
    
    # The following ensures data consistency in the energy consumption column.
    
    xdf[3] = xdf[3].astype(float)
    
    # Construct a pivot table for the sums.
    
    xdf1 = pd.pivot_table(xdf, values=[3], index=[2], columns=[5], \
                         aggfunc= np.sum, fill_value = 0.0)
    xdf1.columns = [aa[1] for aa in xdf1.columns]
    xdf1["total"] = xdf1.sum(axis = 1)
    
    # Construct a pivot table for the counts.
    # fill_value = 1 helps us to avoid a divide by zero error.
    
    xdf2 = pd.pivot_table(xdf, values=[3], index=[2], columns=[5], \
                         aggfunc= len, fill_value = 1)
    xdf2.columns = [aa[1] for aa in xdf2.columns]
    xdf2["total"] = xdf2.sum(axis = 1)
    
    # The right suffix is intentionally labeled 'mean' even
    # though (at this point) the column represents a count.
    
    xdf = xdf1.join(xdf2, rsuffix='_mean', how = 'inner')
    
    # Rename the first half of the columns.
    # Note that the calculation x/2 produces a float value.
    # Perform a process based on the first half of the columns.
    # Adding one to the total number of columns and then dividing 
    # by 2 will prevent spurious instances of rounding down due to
    # a divide by two being marginally less than the exact value.
        
    ncols = int((len(xdf.columns) + 1)/2)
    
    for idx, cn in enumerate(xdf.columns[0:ncols]):
        xdf[cn+"_mean"] = xdf[cn] / xdf[cn+"_mean"]

    xdf.rename(columns = {"total_mean":"mean"}, inplace = True)    
    
  
    xdf.index.name = 'timestamp'
    
    # Create day, month, time columns.
    
    xdf.insert(0, 'year',  xdf.index.map(lambda row: int(row[0:4])))
    xdf.insert(0, 'month', xdf.index.map(lambda row: int(row[5:7])))
    xdf.insert(0, 'day',   xdf.index.map(lambda row: int(row[8:10])))
    xdf.insert(0, 'time',  xdf.index.map(lambda row: row[11:16]))
   
    xdf.fillna(value = 0.0, inplace = True)
    
    xdf.to_csv(outfile)    