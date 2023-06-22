import csv
import PySimpleGUI as sg
from datetime import datetime
from get_weather import get_weather_data
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import json

def get_airport_codes():
    with open('airport-codes.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row['ident'] for row in reader]

def currentDate(returnType='tuple'):
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]
    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }



def print_in_table(formatted_html):


    html_doc = formatted_html
    print(formatted_html)
    soup = BeautifulSoup(html_doc, 'html.parser')
    # Create an empty list to hold our table data
    data = []
    # Find the main table and loop over its rows
    for row in soup.find('table').find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            # Find any nested tables within the cell and get their data
            nested_table = cell.find('table')
            if nested_table:
                nested_data = [nested_cell.get_text(strip=True) for nested_cell in nested_table.find_all('td')]
                row_data.append(nested_data)
            else:
                row_data.append(cell.get_text(strip=True))
        data.append(row_data)

    # Print the data for debug purposes
    '''
    for row in data[2:]:
        print(row)
    '''
    # Convert our data into a format that PySimpleGUI can use
    # We're creating a list of lists, where each sub-list is a row in the table
    table_data = [list(map(str, row)) for row in data[2:]]

    # Create the PySimpleGUI window
    layout = [
        [sg.Table(values=table_data, headings=["Time", "Temperature (°F)", "Dew Point (°F)", "Humidity (%)", "Wind Speed (mph)", "Pressure (in)", "Precipitation (in)"],
                  display_row_numbers=False, auto_size_columns=True,
                  num_rows=min(25, len(table_data)), key='-TABLE-', row_height=35)]
    ]
    window = sg.Window('Table', layout, location=(0,0), resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()
    
def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    current_month,current_day,current_year = currentDate('tuple')
    [sg.Text('Airport Code'), sg.Combo(get_airport_codes(), size=(20, 1))],

    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year
    
    layout = [
        [sg.Text('Month'), sg.Combo(list(range(1, 13)), size=(20, 1))],
        [sg.Text('Day'), sg.Combo(list(range(1, 32)), size=(20, 1))],
        [sg.Text('Year'), sg.Combo(list(range(2000, 2024)), size=(20, 1))],
        [sg.Text('Airport Code'), sg.Combo(get_airport_codes(), size=(20, 1))],
        [sg.Text('Frequency'), sg.Combo(['daily', 'weekly', 'monthly'], size=(20, 1))],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    window = sg.Window('Get The Weather', layout)    

    event, values = window.read()
    window.close()
    
    if event == "Submit":
        month, day, year, code, filter = values.values()
        url = f"https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month}-{day}"
        weather_data = get_weather_data(url)
        
        if weather_data is None:
            sg.popup('Error', 'No weather data found')
            return
        
        print_in_table(formatted_html=weather_data)

if __name__=='__main__':
    buildWeatherURL()

