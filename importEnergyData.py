def importEnergyData():
    
    # It is assumed at this stage that Power-Networks-LCL-June2015(withAcornGps).zip has been downloaded from
    # data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households
    
    from zipfile import ZipFile 
        
    with ZipFile('Power-Networks-LCL-June2015(withAcornGps).zip', 'r') as zip: 
    
        print("The zip file contains ...")
        zip.printdir()     # Prints contents of the zip file.
      
        # extracting all the files 
        print("Extracting the csv file ...") 
        zip.extractall() 
              
        print('Finished extracting csv file.') 
    	
    # 'ToU' time of use
    # 'Std' standard
    
    # Split the large .csv file containing all the data into smaller csv files
    # containing data specific to a specific year and a specific month.
	
    print('Creating monthly data files ...')
    
    with open("Power-Networks-LCL-June2015(withAcornGps)v2.csv") as file, open('data.csv', "w") as ofile: 
        
        # Create a dictionary to store file handles with tuple keys (year, month).
        fileList = {}
        
        # Read the CSV header. 
        line = next(file)
    
        for line in file:
            
            year  = line[14:18]
            month = line[19:21]
            
            # Grab the file handle associate with this year, month pair.
            resp = fileList.get((year, month))
    
            if resp == None:
                # File has not been created for this year, month pair.
                # So create it and store in the dictionary.
                
                fname = 'data_' + year + month + '.csv'
                print('Creating ', fname, " ...")
                fym = open(fname, "w")
                fileList[(year, month)] = (fym, fname)
                xf = fym
            else:
                xf = resp[0]
                
            xf.write(line)
    
    # Close all the files that were created based on year, month pair. This will force
    # a flush of any remaining items left in the stream.
    
    for x in fileList:
        fileList[x][0].close()
    
    from cleanAndProcessEnergyData import cleanAndProcessEnergyData
	
    print('Clean and aggregate monthly data ...' )
    
    xFileList = {}
    
    for key, val in fileList.items():   
        infile = val[1]
        print('Processing ', infile)
        outfile = val[1][0:-4] + "_proc.csv"
        cleanAndProcessEnergyData(infile, outfile)
        print('Created ', outfile)
        xFileList[key] = (infile, outfile)
    	
    	
    import pandas as pd
    dfs = pd.DataFrame(xFileList)
    dfs = dfs.transpose()
    dfs.reset_index(inplace = True)
    dfs.columns = ["year", "month", "raw", "processed"]
    
    # Serialize the file directory.
    
    dfs.to_csv("./fileList.csv", index = False)


