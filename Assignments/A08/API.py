from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
import pandas as pd
from fastapi import FastAPI, Query

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
### Swaraj Chirumamilla
"""

class DataReader:
    def __init__(self, csv_file):
        self.data = None
        self.load_data(csv_file)

    def load_data(self, csv_file):
        try:
            self.data = pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"Error: File {csv_file} not found.")
            self.data = None

    def get_attribute(self, attribute):
        return json.dumps(self.data[attribute].unique().tolist())

    def get_unique_countries(self):
        unique_countries = self.data["Country"].unique().tolist()
        return unique_countries

    def get_available_regions(self):
        available_regions = self.data["WHO_region"].unique().tolist()
        return available_regions


# Instantiate the DataReader class with the CSV file path
mydb = DataReader(r'C:\Users\swara\OneDrive\Desktop\assignemnet\data.csv')

# print(mydb.data.head())
# print(mydb.data.shape[0])

# Initialize the FastAPI app with the provided description
app = FastAPI(description=description)

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():
    unique_countries = mydb.get_unique_countries()
    return {"countries": unique_countries}

@app.get("/regions")
def regions():
    available_regions = mydb.get_available_regions()
    return {"regions": available_regions}

@app.get("/deaths/")
async def deaths(country:str = None,year:int = None,region:str = None):
    """
    This method will return a total death count or can be filtered by country and year.
    - Params:
      - country (str) : A country name
      - year (int) : A 4 digit year
      - region (str) : A region name
    - **Returns:**
      - (int) : The total sum of deaths based on filters (if any)
    """
    response=int(mydb.data['New_deaths'].sum())
    message=f"Total number of entire deaths {response}"
    if year!=None:
        # response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_deaths'].sum())
        if country!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['Country'] == country), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} for the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['WHO_region'] == region), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} in the WHO region in {region} is {response}"
        else:
            response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_deaths'].sum())
            message=f"Total number of deaths in {year} is {response}"
    else:
        if country!=None:
            response=int(mydb.data[mydb.data['Country'] == country]['New_deaths'].sum())
            message=f"Total number of deaths in the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data[mydb.data['WHO_region'] == region]['New_deaths'].sum())
            message=f"Total number of deaths in the WHO region of {region} is {response}"

    return {"deaths": response, "message": message}


@app.get("/cases/")
async def cases(country:str = None,year:int = None,region:str = None):
    """
    This method will return a total death count or can be filtered by country and year.
    - Params:
      - country (str) : A country name
      - year (int) : A 4 digit year
      - region (str) : A region name
    - **Returns:**
      - (int) : The total sum of cases based on filters (if any)
    """
    response=int(mydb.data['New_cases'].sum())
    message=f"Total number of entire cases {response}"
    if year!=None:
        # response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_cases'].sum())
        if country!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['Country'] == country), 'New_cases'].sum())
            message=f"Total number of cases in {year} in the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data.loc[(pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year)) & (mydb.data['WHO_region'] == region), 'New_cases'].sum())
            message=f"Total number of cases in {year} in the WHO region in {region} is {response}"
        else:
            response=int(mydb.data.loc[pd.to_datetime(mydb.data['Date_reported']).dt.year == int(year), 'New_cases'].sum())
            message=f"Total number of cases in {year} is {response}"
    else:
        if country!=None:
            response=int(mydb.data[mydb.data['Country'] == country]['New_cases'].sum())
            message=f"Total number of cases in the country of {country} is {response}"
        if region!=None:
            response=int(mydb.data[mydb.data['WHO_region'] == region]['New_cases'].sum())
            message=f"Total number of cases in the WHO region of {region} is {response}"

    return {"cases": response, "message": message}



@app.get("/max_deaths")
async def max_deaths(min_date: str = Query(None, description="Minimum date (YYYY-MM-DD)"),
                     max_date: str = Query(None, description="Maximum date (YYYY-MM-DD)")):
    """
    Finds the country with the most deaths and the country with the most deaths between a range of dates.

    Parameters:
    - min_date (str): Minimum date (YYYY-MM-DD) (optional).
    - max_date (str): Maximum date (YYYY-MM-DD) (optional).

    Returns:
    - (dict): A dictionary containing the country with the most deaths.
    """
    if min_date is None and max_date is None:
        # Find the country with the overall most deaths
        country_with_most_deaths = mydb.data.loc[mydb.data["Cumulative_deaths"].idxmax(), "Country"]
        return {"country_with_most_deaths": country_with_most_deaths}
    elif min_date is not None and max_date is not None:
        # Find the country with the most deaths between the given range of dates
        filtered_data = mydb.data[(mydb.data["Date_reported"] >= min_date) & (mydb.data["Date_reported"] <= max_date)]
        country_with_most_deaths = filtered_data.loc[filtered_data["Cumulative_deaths"].idxmax(), "Country"]
        return {"country_with_most_deaths": country_with_most_deaths}
    else:
        return {"error": "Both min_date and max_date must be provided."}

@app.get("/min_deaths")
async def min_deaths(min_date: str = Query(None, description="Minimum date (YYYY-MM-DD)"),
                     max_date: str = Query(None, description="Maximum date (YYYY-MM-DD)")):
    """
    Finds the country with the fewest deaths and the country with the fewest deaths between a range of dates.

    Parameters:
    - min_date (str): Minimum date (YYYY-MM-DD) (optional).
    - max_date (str): Maximum date (YYYY-MM-DD) (optional).

    Returns:
    - (dict): A dictionary containing the country with the fewest deaths.
    """
    if min_date is None and max_date is None:
        # Find the country with the overall fewest deaths
        country_with_fewest_deaths = mydb.data.loc[mydb.data["Cumulative_deaths"].idxmin(), "Country"]
        return {"country_with_fewest_deaths": country_with_fewest_deaths}
    elif min_date is not None and max_date is not None:
        # Find the country with the fewest deaths between the given range of dates
        filtered_data = mydb.data[(mydb.data["Date_reported"] >= min_date) & (mydb.data["Date_reported"] <= max_date)]
        country_with_fewest_deaths = filtered_data.loc[filtered_data["Cumulative_deaths"].idxmin(), "Country"]
        return {"country_with_fewest_deaths": country_with_fewest_deaths}
    else:
        return {"error": "Both min_date and max_date must be provided."}




if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True) #host="127.0.0.1"
