def downloadEnergyData():

    import urllib.request
    
    print('Beginning file download ...')
    
    url = "https://data.london.gov.uk/download/smartmeter-energy-use-data-in-london-households/3527bf39-d93e-4071-8451-df2ade1ea4f2/Power-Networks-LCL-June2015(withAcornGps).zip"
    
    #urllib.request.urlretrieve(url, './data.zip')
    
    urllib.request.urlretrieve(url, './Power-Networks-LCL-June2015(withAcornGps).zip')