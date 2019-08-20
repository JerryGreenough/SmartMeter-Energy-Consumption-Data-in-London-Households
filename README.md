# SmartMeter Energy Consumption in London Households

This project demonstrates how Python is used in the processing and visualization of SmartMeter Energy Consumption Data from the Low Carbon London project. The majority of the data processing makes use of the Pandas module. The visualization is undertaken with multi-line plots created using the Matplotlib module. The project was initiated by and undertaken with the help of Michael Blackmon (https://www.linkedin.com/in/michael-blackmon-b4431263).

The Low Carbon London project was led by UK Power Networks, a company that owns and maintains electricity cables and lines across London, the South East and East of England. As part of the LCL project, energy consumption readings were taken for a sample of 5,567 London Households between November 2011 and February 2014.

The line plot shown below demonstrates typical graphical output that can be generated once the data has been cleaned and aggregated. It depicts the average energy consumption at a given time stamp for a sample of months (January through July for 2013).

![Average monthly energy consumption during a typical day](https://raw.githubusercontent.com/JerryGreenough/SmartMeter-Energy-Consumption-Data-in-London-Households/master/MonthlyAverage.png)

The summer months (April through July) demonstrate a tendency for the peak of the energy consumption to occur at approximately the same time as sunset (data available from http://www.timeanddate.com). However, the same trend cannot be observed as strongly for the winter months (January through March), which all peak at roughly the same time stamp (19:15). Sunset for the winter months takes place much earlier in the day. It is conjectured that electrical draws associated with heating and cooking are less subject to time variation during the winter months and might explain the lack of variability in the time stamp of the peak energy consumption.

## Data Source

The SmartMeter data has been made available on the following site.

https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households

This site allows the viewer to download a zip file of size 783 MB that contains an 11.3 GB CSV(comma seperated values) file with 167 million rows of data. The CSV file contains measurements of energy consumption in kW-h taken every half hour for each customer over a period of about two years. Furthermore, each customer is assigned an Acorn designation and a prosperity categor based on the Acorn designation. 

Acorn (developed by CACI Ltd in the UK) segments UK postcodes and neighborhoods into 6 Categories, 18 Groups and 62 types, three of which are not private households. By analyzing significant social factors and population behavior, it provides precise information and in-depth understanding of the different types of people (https://en.wikipedia.org/wiki/Acorn_(demographics)).

The unzipping of the downloaded file can be achieved using standard operating system utilities. However, it can also be undertaken with  Python code by using the ZipFile module. This is illustrated by the following code taken from ```importEnergyData.py```.

```python
from zipfile import ZipFile 
        
    with ZipFile('Power-Networks-LCL-June2015(withAcornGps).zip', 'r') as zip: 
  
        print("Extracting the csv file ...") 
        zip.extractall() 
```

There is a challenge in cleaning and aggregating the data so that either the total or mean energy usage (taken over all participating customers) can be calculated and thence visualized. Most notably, the sheer size of the data does not lend itself to successful in-memory manipulation using Pandas. Therefore, the first step in processing the data is to split it into 28 separate CSV files, each representing energy consumption data for all registered customers for each month of each year (Nov 2011 - Feb 2014). The Python code required to do this is contained in the top half of the file ```importEnergyData.py``` (line 27).

## Data Cleaning

Once the data has been split into bit-size pieces, the next challenge is to clean the data. The Python code required to do this is contained in the file ```cleanAndProcessEnergyData.py```, which contains an eponymous function that accepts one of the 28 uncleaned and unaggregated monthly CSV files and outputs a cleaned and aggregated version that can then be used for additional calculations and/or visualization.

The data cleaning operations include:
* Dropping rows that contain null and NaN values
* Eliminating duplicate rows (corresponding to duplicate SmartMeter reports)
* Elimination of Time-of-Use data.

Time-of-Use metering entails the employment of an array of energy rates based on the time of day in which the energy is being consumed. It is elminated in order to prevent the time-dependent energy tariff from influencing the fundamental daily trends shown by the energy consumption data.

## Data Aggregation

The remainder of the Python code contained in ```cleanAndProcessEnergyData.py``` is devoted to grouping energy consumption records by timestamp in order to calculate the total and mean energy consumption (per timestamp) over all customers for any given day.

An elegant way to this is to use a Pandas pivot table to collect energy sums and measurement counts based on grouping the meter reports by both timestamp and prosperity group. The pivot table is a two-dimensional equivalent to the Pandas groupby functionality.

```Python
# Construct a pivot table for the sums.
# fill_value = 0.0 provides for a meaningful value to be inserted for the case in which 
# no measurement reports are made for a particular grouping.

xdf1 = pd.pivot_table(xdf, values=["energy"], index=["time"], columns=["prosperity group"], \
                         aggfunc= np.sum, fill_value = 0.0)
xdf1["total"] = xdf1.sum(axis = 1)

# Construct a pivot table for the counts.
# fill_value = 1 helps us to avoid a divide by zero error for the case in which no measuremet
# reports are made for a particular grouping.

xdf2 = pd.pivot_table(xdf, values=["energy"], index=["time"], columns=["prosperity group"], \
                         aggfunc= len, fill_value = 1)
xdf2["total"] = xdf2.sum(axis = 1)
```
The sum of the energy sums and their associated counts are also calculated in each respective Pandas dataframe. The ```axis=1``` argument ensures that summation is peformed across the columns for any given row. The two tables are subsequently inner-joined in order for mean energy usage to be calculated. The join operation is performed on equivalence of the index column of each dataframe using the Pandas dataframe ```.join``` function.

It is now a straightforward to perform a calculation of mean usage at a given time point (i) for all customers within a specific prosperity group and (ii) for the totality of customers over all prosperity groups. 






