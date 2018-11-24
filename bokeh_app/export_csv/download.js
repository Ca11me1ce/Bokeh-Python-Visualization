var data = source.data;
var filetext = 'name,' +
    'latitude,' +
    'longitude,' +
    'zipcode,' +
    'city,' +
    'state,' +
    'price,' +
    'rating,' +
    'review_count,' +
    'category_x,' +
    'Accept_Credit_Card,' +
    'Alcohol,' +
    'Outdoor_Seating,' +
    'Parking,' +
    'Take_out,' +
    'Takes_Reservations,' +
    'WIFI,' +
    'Ambience,' +
    'Attire,' +
    'Noise_Level,' +
    'atm,' +
    'bank,' +
    'bar,' +
    'beauty_salon,' +
    'bus_station,' +
    'cafe,' +
    'gym,' +
    'school,' +
    'White_population,' +
    'Black_population,' +
    'American_Indian_population,' +
    'Asian_population,' +
    'Hispanic_or_Latino_population,' +
    'High_school_or_higher,' +
    'Graduate_or_professional_degree,' +
    'Unemployed,' +
    'average_price,' +
    'review_count_binned\n';
for (var i = 0; i < data['name'].length; i++) {
    var currRow = [data['name'][i].toString(),
                   data['latitude'][i].toString(),
                   data['longitude'][i].toString(),
        data['zipcode'][i].toString(),
        data['city'][i].toString(),
        data['state'][i].toString(),
        data['price'][i].toString(),
        data['rating'][i].toString(),
        data['review_count'][i].toString(),
        data['category_x'][i].toString(),
        data['Accept_Credit_Card'][i].toString(),
        data['Alcohol'][i].toString(),
        data['Outdoor_Seating'][i].toString(),
        data['Take_out'][i].toString(),
        data['Takes_Reservations'][i].toString(),
        data['WIFI'][i].toString(),
        data['Ambience'][i].toString(),
        data['Attire'][i].toString(),
        data['Noise_Level'][i].toString(),
        data['atm'][i].toString(),
        data['bank'][i].toString(),
        data['bar'][i].toString(),
        data['beauty_salon'][i].toString(),
        data['bus_station'][i].toString(),
        data['cafe'][i].toString(),
        data['gym'][i].toString(),
        data['school'][i].toString(),
        data['White_population'][i].toString(),
        data['Black_population'][i].toString(),
        data['American_Indian_population'][i].toString(),
        data['Asian_population'][i].toString(),
        data['Hispanic_or_Latino_population'][i].toString(),
        data['High_school_or_higher'][i].toString(),
        data['Graduate_or_professional_degree'][i].toString(),
        data['Unemployed'][i].toString(),
        data['average_price'][i].toString(),

        data['review_count_binned'][i].toString().concat('\n')];





    var joined = currRow.join();
    filetext = filetext.concat(joined);
}

var filename = 'data_result.csv';
var blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' });

//addresses IE
if (navigator.msSaveBlob) {
    navigator.msSaveBlob(blob, filename);
} else {
    var link = document.createElement("a");
    link = document.createElement('a')
    link.href = URL.createObjectURL(blob);
    link.download = filename
    link.target = "_blank";
    link.style.visibility = 'hidden';
    link.dispatchEvent(new MouseEvent('click'))
}
