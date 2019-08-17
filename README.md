# SmartMeter Energy Consumption in London Households

This project demonstrates how Python was used in the processing and visualization of SmartMeter Energy Consumption Data from the Low Carbon London project. The majority of the data processing makes use of the Pandas module. The visualization is undertaken with multi-line plots created using the Matplotlib module. The project was initiated by and undertaken with Michael Blackmon (https://www.linkedin.com/in/michael-blackmon-b4431263).

The Low Carbon London project was led by UK Power Networks, a company that owns and maintains electricity cables and lines across London, the South East and East of England. As part of the LCL project, energy consumption readings were taken for a sample of 5,567 London Households between November 2011 and February 2014.

The line plot shown below demonstrates typical graphical output that can be generated once the data has been cleaned and aggregated. It depicts the average energy consumption at a given time stamp for a sample of months (January through July for 2013).

![Average monthly energy consumption during a typical day](https://raw.githubusercontent.com/JerryGreenough/SmartMeter-Energy-Consumption-Data-in-London-Households/master/MonthlyAverage.png)

The summer months (April through July) demonstrate a tendency for the peak of the energy consumption to occur at approximately the same time as sunset (data available from http://www.timeanddate.com). However, the same trend cannot be observed as strongly for the winter months (January through March), which all peak at roughly the same time stamp (19:15). Sunset for the winter months takes place much earlier in the day. It is conjectured that electrical draws associated with heating and cooking are less subject to time variation during the winter months and might explain the lack of variability in the time stamp of the peak energy consumption.

## Data Source

The SmartMeter data has been made available on the following site.

https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households

This site allows the viewer to download a zip file of size 783 MB that contains an 11.3 GB CSV(comma seperated values) file with 167 million rows of data. The CSV file contains measurements of energy consumption in kW-h taken every half hour for each customer over a period of about two years.

The unzipping of the downloaded file can be achieved using standard operating system utilities. However, it can also be undertaken with  Python code by using the ZipFile module. This is illustrated by the following code taken from importEnergyData.py.

```
from zipfile import ZipFile 
        
    with ZipFile('Power-Networks-LCL-June2015(withAcornGps).zip', 'r') as zip: 
  
        print("Extracting the csv file ...") 
        zip.extractall() 
```

There is a challenge in cleaning and aggregating the data so that either the total or mean energy usage (taken over all participating customers) can be calculated and thence visualized. Most notably, the sheer size of the data does not lend itself to successful in-memory manipulation using Pandas. Therefore, the first step in processing the data is to split it into 28 separate CSV files, each representing energy consumption data for all registered customers for each month of each year (Nov 2011 - Feb 2014). The Python code required to do this is contained in the top half of the file importEnergyData.py (line 27).

## Data Cleaning and Aggregation

Once the data has been split into bit-size pieces, the next challenge is to clean the data. The Python code required to do this is contained in the file [cleanAndProcessEnergyData.py], which contains an eponymous function that accepts one of the 28 uncleaned and unaggregated monthly CSV files and outputs a cleaned and aggregated version that can then be used for additional calculations and/or visualization.

The data cleaning operations include:
* Dropping rows that contain NaN values
* Eliminating duplicate rows (corresponding to duplicate SmartMeter reports)
* Elimination of Time-of-Use data.

Time-of-Use metering entails the employment of an array of energy rates based on the time of day in which the energy is being consumed. it is elminated in order to prevent the time-dependent energy tariff from influencing the fundamental daily trends shown by the energy consumption data.

