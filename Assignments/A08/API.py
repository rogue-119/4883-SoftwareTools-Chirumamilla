from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
import pandas as pd

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
        self.data = pd.read_csv(csv_file)

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




if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True) #host="127.0.0.1"
