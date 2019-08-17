# SmartMeter Energy Consumption in London Households

This project demonstrates how Python was used in the processing and visualization of SmartMeter Energy Consumption Data from the Low Carbon London project. The majority of the data processing makes use of the Pandas module. The visualization is undertaken with multi-line plots created using the Matplotlib module.

The Low Carbon London project was led by UK Power Networks, a company that owns and maintains electricity cables and lines across London, the South East and East of England. As part of the LCL project, energy consumption readings were taken for a sample of 5,567 London Households between November 2011 and February 2014.

The line plot shown below demonstrates typical graphical output that can be generated once the data has been cleaned and aggregated. It depicts the average energy consumption at a given time stamp for a sample of months (January through July for 2013).

![Average monthly energy consumption during a typical day](https://raw.githubusercontent.com/JerryGreenough/SmartMeter-Energy-Consumption-Data-in-London-Households/master/MonthlyAverage.png)

The summer months (April through July) demonstrate a tendency for the peak of the energy consumption to occur at approximately the same time as sunset (data available from http://www.timeanddate.com). However, the same trend cannot be observed as strongly for the winter months (January through March), which all peak at roughly the same time stamp (19:15). Sunset for the winter months takes place much earlier in the day. It is conjectured that electrical draws associated with heating and cooking are less subject to time variation during the winter months and might explain the lack of variability in the time stamp of the peak energy consumption.

## Data Source

The SmartMeter data has been made available on the following site.

https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households

It is a zip file of size 783 MB that contains an 11.3 GB CSV(comma seperated values) file with 167 million rows of data.

