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

 Route: /
- Retrieves the documentation provided by swagger.

 Route: /countries
- Retrieves a list of unique countries from the "db"

- Route: /regions
Retrieves a list of available WHO regions from the "db"

- Route: /deaths
Retrieves total deaths for all countries,for the given country, WHO region and year

- Route: /cases
Retrieves total casess for all countries,for the given country, WHO region and year

- Route: /max_deaths
Find the country with the most deaths between a range of dates

-Route: /min_deaths
Find the country with the least deaths between a range of dates

-Route: /avg_deaths
Find the average number of deaths between all countries

 #### Example

- Request: GET `/regions/`
#### Example 1: [http://127.0.0.1:5000/regions](http://127.0.0.1:5000/regions)
    ### Response:               
                  {
                    "regions": [
                            "EMRO",
                            "EURO",
                            "AFRO",
                            "WPRO",
                            "AMRO",
                            "SEARO",
                            "Other"
                            ]
                   }


                   
- Request: GET `/deaths/` 
#### Example 2: [http://127.0.0.1:5000/deaths/?country=India&year=2020](http://127.0.0.1:5000/deaths/?country=India&year=2020)
    ### Response:
             { "deaths": 1946775,
              "message": "Total number of deaths in 2020 is 1946775"}


- Request: GET `/cases/`
#### Example 3: [http://127.0.0.1:5000/cases/?country=China&year=2020](http://127.0.0.1:5000/cases/?country=China&year=2020)
      ### Response:
              {
                "cases": 82853510,
                "message": "Total number of cases in 2020 is 82853510"
               }

- Request: GET `/max_deaths/` 
#### Example 4: [http://127.0.0.1:5000/max_deaths?min_date=2020-03-24&max_date=2021-06-21](http://127.0.0.1:5000/max_deaths?min_date=2020-03-24&max_date=2021-06-21)
          ### Response:
                {
                    "country_with_most_deaths": "United States of America"
                 }

- Request: GET `/min_deaths/` 
#### Example 5: [http://127.0.0.1:5000/min_deaths?min_date=2020-04-24&max_date=2021-06-21](http://127.0.0.1:5000/min_deaths?min_date=2020-04-24&max_date=2021-06-21)
          ### Response:
          {
              "country_with_fewest_deaths": "American Samoa"
          }   
          
- Request: GET `/average_deaths/` 
#### Example 6: [http://127.0.0.1:5000/average_deaths?country1=Afghanistan&country2=China](http://127.0.0.1:5000/average_deaths?country1=Afghanistan&country2=China)
        ### Response:
        {
           "average_deaths": 
            "Afghanistan": 6.257503949447077,
             "China": 95.88467614533965
                  
         }
## Instructions

- Install all dependencies from requirments.txt
-  Please change the data.csv file path which is given in line number 40.
 
### Challenges Faced 

- Was getting Server errors in the process of writing Deaths function, solved it through trobleshooting and took help of ChatGPT while writing the deaths Function and the maximum no. of deaths Endpoint.

