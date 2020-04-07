# EV Commute Calculator
Electric Vehicle Commute Calculator is a linear model which calculates roughly what percentage of an electric vehicle's available battery charge will be consumed in a given trip, based on the following input parameters:
* Battery Capacity (in kWh)
* Vehicle Range (in km)
* Gross Vehicle Weight (including people and luggage)
* Trip distance (in m) - this is assumed to be a horizontal only component,
* Change in elevation (in m) - the sum of all changes in elevation\
The latter two parameters can be acquired (for example) by entering a given trip in (Google Maps)[https://www.google.com/maps] using the Cycling Option
The model is generalised for any type of electric vehicle (e.g. electric cars, bikes or skateboards)
