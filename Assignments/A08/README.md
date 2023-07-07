# A08 - Fast Api with Covid Data
## Swaraj Chirumamilla
## Overview:

Created a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.


## Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   |  [api.py](https://github.com/swarajtwok/4883-SoftwareTools-Chirumamilla/blob/main/Assignments/A08/api.py)  |   code file  |
|   2 | [data.csv](https://github.com/swarajtwok/4883-SoftwareTools-Chirumamilla/blob/main/Assignments/A08/data.csv) | the covid csv data file |
|    3 | [requirements](https://github.com/swarajtwok/4883-SoftwareTools-Chirumamilla/blob/main/Assignments/A08/requirements.txt) | requirements needed to install to run code|

## Fast API Endpoints

 #### Example

- Request: GET `/regions/`
  
{"data":{"EMRO":351329},
                     "success":true,
                     "message":"Deaths of Region",
                     "Region":"EMRO",
                     "country":null,
                     "year":null}

                     
## Instructions

- Install all dependencies from requirments.txt
-  Please change the data.csv file path which is given in line number 40.
 


