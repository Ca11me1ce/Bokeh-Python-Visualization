from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS, Panel
from bokeh.models.widgets import RangeSlider, Button, DataTable, TableColumn, NumberFormatter
from bokeh.io import curdoc

df = pd.read_csv(join(dirname(__file__), 'Full_Information_Cleaned.csv'))


source = ColumnDataSource(data=dict())

def update():
    current = df.dropna()
    #source.data is used for downloading with js file
    source.data = {
        'name'             : current.name,
        'latitude': current.latitude,
        'longitude': current.longitude,
        'zipcode' : current.zipcode,
        'city': current.city,
        'state': current.state,
        'price': current.price,
        'rating': current.rating,
        'review_count'           : current.review_count,
        'category_x': current.category_x,
        'Accept_Credit_Card': current.Accept_Credit_Card,
        'Alcohol': current.Alcohol,
        'Outdoor_Seating': current.Outdoor_Seating,
        'Parking': current.Parking,
        'Take_out': current.Take_out,
        'Takes_Reservations': current.Takes_Reservations,
        'WIFI': current.WIFI,
        'Ambience': current.Ambience,
        'Attire': current.Attire,
        'Noise_Level': current.Noise_Level,
        'atm': current.atm,
        'bank': current.bank,
        'bar': current.bar,
        'beauty_salon': current.beauty_salon,
        'bus_station': current.bus_station,
        'cafe': current.cafe,
        'gym': current.gym,
        'school': current.school,
        'White_population': current.White_population,
        'Black_population': current.Black_population,
        'American_Indian_population': current.American_Indian_population,
        'Asian_population': current.Asian_population,
        'Hispanic_or_Latino_population': current.Hispanic_or_Latino_population,
        'High_school_or_higher': current.High_school_or_higher,
        'Graduate_or_professional_degree': current.Graduate_or_professional_degree,
        'Unemployed': current.Unemployed,
        'average_price': current.average_price,
        'review_count_binned': current.review_count_binned,

        
    }


def export_csv():
    #slider = RangeSlider(title="Review Count", start=10, end=3000, value=(10, 100), step=100, format="0,0")
    #slider.on_change('value', lambda attr, old, new: update(slider))

    button = Button(label="Download", button_type="success")
    button.callback = CustomJS(args=dict(source=source),
                            code=open(join(dirname(__file__), "download.js")).read())

    columns = [
        TableColumn(field="name", title="Restaurant Name"),
        TableColumn(field="latitude", title="Latitude", formatter=NumberFormatter(format="0,0.0000")),
        TableColumn(field="longitude", title="Longitude", formatter=NumberFormatter(format="0,0.0000")),
        TableColumn(field="zipcode", title="Zipcode"),
        TableColumn(field="city", title="City"),
        TableColumn(field="state", title="State"),
        TableColumn(field="price", title="Price"),
        TableColumn(field="rating", title="Rating", formatter=NumberFormatter(format="0,0.0")),
        TableColumn(field="review_count", title="Review Count", formatter=NumberFormatter(format="0,0")),
        TableColumn(field="category_x", title="Category"),
        TableColumn(field="Accept_Credit_Card", title="Accept Credit Card"),
        TableColumn(field="Alcohol", title="Alcohol"),
        TableColumn(field="Outdoor_Seating", title="Outdoor Seating"),
        TableColumn(field="Parking", title="Parking"),
        TableColumn(field="Take_out", title="Take Out"),
        TableColumn(field="Takes_Reservations", title="Takes Reservations"),
        TableColumn(field="WIFI", title="WIFI"),
        TableColumn(field="Ambience", title="Ambience"),
        TableColumn(field="Attire", title="Attire"),
        TableColumn(field="Noise_Level", title="Noise Level"),
        TableColumn(field="atm", title="ATM"),
        TableColumn(field="bank", title="Bank"),
        TableColumn(field="bar", title="bar"),
        TableColumn(field="beauty_salon", title="Beauty Salon"),
        TableColumn(field="bus_station", title="Bus Station"),
        TableColumn(field="cafe", title="Cafe"),
        TableColumn(field="gym", title="Gym"),
        TableColumn(field="school", title="School"),
        TableColumn(field="White_population", title="White Population", formatter=NumberFormatter(format="0,0.000000")),
        TableColumn(field="Black_population", title="Black Population", formatter=NumberFormatter(format="0,0.000000")),
        TableColumn(field="American_Indian_population", title="American Indian Population", formatter=NumberFormatter(format="0,0.000000")),
        TableColumn(field="Asian_population", title="Asian Population", formatter=NumberFormatter(format="0,0.000000")),
        TableColumn(field="Hispanic_or_Latino_population", title="Hispanic or Latino Population", formatter=NumberFormatter(format="0,0.000000")),
        TableColumn(field="High_school_or_higher", title="High School or Higher", formatter=NumberFormatter(format="0,0.000")),
        TableColumn(field="Graduate_or_professional_degree", title="Graduate or Professional Degree", formatter=NumberFormatter(format="0,0.000")),
        TableColumn(field="Unemployed", title="Unemployed", formatter=NumberFormatter(format="0,0.000")),
        TableColumn(field="average_price", title="Average Price", formatter=NumberFormatter(format="$0,0")),
        TableColumn(field="review_count_binned", title="Review Count Binned"),

        
        
        
    ]

    data_table = DataTable(source=source, columns=columns, fit_columns=False, width=800, height=1000)

    controls = widgetbox(button)
    table = widgetbox(data_table)

    layout = row(controls, table)
    tab = Panel(child=layout, title = 'Export CSV')

    update()
    return tab
