from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/p2")
def page2():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    my_name = "Rafin"
    return render_template('page2.html', this_guy=my_name, current_time=current_time)

@app.route("/bio")
def bio():
    return render_template('bio.html')

@app.route('/world-clock', methods=['GET', 'POST'])
def world_clock():
    available_cities = {
        # North America
        'New York': 'America/New_York',
        'Los Angeles': 'America/Los_Angeles',
        'Chicago': 'America/Chicago',
        'Toronto': 'America/Toronto',
        'Vancouver': 'America/Vancouver',
        'Montreal': 'America/Montreal',
        'Mexico City': 'America/Mexico_City',
        'Guadalajara': 'America/Mexico_City',
        'Phoenix': 'America/Phoenix',
        'Denver': 'America/Denver',
        'Atlanta': 'America/New_York',
        'Miami': 'America/New_York',
        'Seattle': 'America/Los_Angeles',
        'San Francisco': 'America/Los_Angeles',
        'Las Vegas': 'America/Los_Angeles',
        'Anchorage': 'America/Anchorage',
        'Honolulu': 'Pacific/Honolulu',
        
        # South America
        'São Paulo': 'America/Sao_Paulo',
        'Buenos Aires': 'America/Argentina/Buenos_Aires',
        'Rio de Janeiro': 'America/Sao_Paulo',
        'Lima': 'America/Lima',
        'Bogotá': 'America/Bogota',
        'Santiago': 'America/Santiago',
        'Caracas': 'America/Caracas',
        'Montevideo': 'America/Montevideo',
        'La Paz': 'America/La_Paz',
        'Quito': 'America/Guayaquil',
        
        # Europe
        'London': 'Europe/London',
        'Paris': 'Europe/Paris',
        'Berlin': 'Europe/Berlin',
        'Rome': 'Europe/Rome',
        'Madrid': 'Europe/Madrid',
        'Amsterdam': 'Europe/Amsterdam',
        'Brussels': 'Europe/Brussels',
        'Vienna': 'Europe/Vienna',
        'Zurich': 'Europe/Zurich',
        'Stockholm': 'Europe/Stockholm',
        'Oslo': 'Europe/Oslo',
        'Copenhagen': 'Europe/Copenhagen',
        'Helsinki': 'Europe/Helsinki',
        'Warsaw': 'Europe/Warsaw',
        'Prague': 'Europe/Prague',
        'Budapest': 'Europe/Budapest',
        'Bucharest': 'Europe/Bucharest',
        'Athens': 'Europe/Athens',
        'Istanbul': 'Europe/Istanbul',
        'Moscow': 'Europe/Moscow',
        'St. Petersburg': 'Europe/Moscow',
        'Kiev': 'Europe/Kiev',
        'Dublin': 'Europe/Dublin',
        'Lisbon': 'Europe/Lisbon',
        'Barcelona': 'Europe/Madrid',
        'Milan': 'Europe/Rome',
        'Frankfurt': 'Europe/Berlin',
        'Munich': 'Europe/Berlin',
        
        # Asia
        'Tokyo': 'Asia/Tokyo',
        'Shanghai': 'Asia/Shanghai',
        'Mumbai': 'Asia/Kolkata',
        'Delhi': 'Asia/Kolkata',
        'Seoul': 'Asia/Seoul',
        'Bangkok': 'Asia/Bangkok',
        'Singapore': 'Asia/Singapore',
        'Hong Kong': 'Asia/Hong_Kong',
        'Dubai': 'Asia/Dubai',
        'Beijing': 'Asia/Shanghai',
        'Manila': 'Asia/Manila',
        'Jakarta': 'Asia/Jakarta',
        'Kuala Lumpur': 'Asia/Kuala_Lumpur',
        'Taipei': 'Asia/Taipei',
        'Ho Chi Minh City': 'Asia/Ho_Chi_Minh',
        'Hanoi': 'Asia/Ho_Chi_Minh',
        'Osaka': 'Asia/Tokyo',
        'Kolkata': 'Asia/Kolkata',
        'Chennai': 'Asia/Kolkata',
        'Bangalore': 'Asia/Kolkata',
        'Karachi': 'Asia/Karachi',
        'Lahore': 'Asia/Karachi',
        'Islamabad': 'Asia/Karachi',
        'Dhaka': 'Asia/Dhaka',
        'Colombo': 'Asia/Colombo',
        'Kathmandu': 'Asia/Kathmandu',
        'Kabul': 'Asia/Kabul',
        'Tehran': 'Asia/Tehran',
        'Baghdad': 'Asia/Baghdad',
        'Riyadh': 'Asia/Riyadh',
        'Kuwait City': 'Asia/Kuwait',
        'Doha': 'Asia/Qatar',
        'Abu Dhabi': 'Asia/Dubai',
        'Muscat': 'Asia/Muscat',
        'Tashkent': 'Asia/Tashkent',
        'Almaty': 'Asia/Almaty',
        'Bishkek': 'Asia/Bishkek',
        'Yerevan': 'Asia/Yerevan',
        'Baku': 'Asia/Baku',
        'Tbilisi': 'Asia/Tbilisi',
        'Jerusalem': 'Asia/Jerusalem',
        'Tel Aviv': 'Asia/Jerusalem',
        'Beirut': 'Asia/Beirut',
        'Damascus': 'Asia/Damascus',
        'Amman': 'Asia/Amman',
        'Nicosia': 'Asia/Nicosia',
        
        # Africa
        'Cairo': 'Africa/Cairo',
        'Lagos': 'Africa/Lagos',
        'Johannesburg': 'Africa/Johannesburg',
        'Cape Town': 'Africa/Johannesburg',
        'Nairobi': 'Africa/Nairobi',
        'Casablanca': 'Africa/Casablanca',
        'Tunis': 'Africa/Tunis',
        'Algiers': 'Africa/Algiers',
        'Addis Ababa': 'Africa/Addis_Ababa',
        'Dar es Salaam': 'Africa/Dar_es_Salaam',
        'Kampala': 'Africa/Kampala',
        'Kigali': 'Africa/Kigali',
        'Lusaka': 'Africa/Lusaka',
        'Harare': 'Africa/Harare',
        'Windhoek': 'Africa/Windhoek',
        'Gaborone': 'Africa/Gaborone',
        'Maputo': 'Africa/Maputo',
        'Antananarivo': 'Indian/Antananarivo',
        'Port Louis': 'Indian/Mauritius',
        'Dakar': 'Africa/Dakar',
        'Abidjan': 'Africa/Abidjan',
        'Accra': 'Africa/Accra',
        'Bamako': 'Africa/Bamako',
        'Ouagadougou': 'Africa/Ouagadougou',
        'Niamey': 'Africa/Niamey',
        'N\'Djamena': 'Africa/Ndjamena',
        'Libreville': 'Africa/Libreville',
        'Kinshasa': 'Africa/Kinshasa',
        'Luanda': 'Africa/Luanda',
        'Douala': 'Africa/Douala',
        'Brazzaville': 'Africa/Brazzaville',
        'Bangui': 'Africa/Bangui',
        'Malabo': 'Africa/Malabo',
        'Khartoum': 'Africa/Khartoum',
        'Djibouti': 'Africa/Djibouti',
        'Asmara': 'Africa/Asmara',
        'Mogadishu': 'Africa/Mogadishu',
        
        # Oceania
        'Sydney': 'Australia/Sydney',
        'Melbourne': 'Australia/Melbourne',
        'Brisbane': 'Australia/Brisbane',
        'Perth': 'Australia/Perth',
        'Adelaide': 'Australia/Adelaide',
        'Darwin': 'Australia/Darwin',
        'Hobart': 'Australia/Hobart',
        'Canberra': 'Australia/Sydney',
        'Auckland': 'Pacific/Auckland',
        'Wellington': 'Pacific/Auckland',
        'Christchurch': 'Pacific/Auckland',
        'Suva': 'Pacific/Fiji',
        'Port Moresby': 'Pacific/Port_Moresby',
        'Noumea': 'Pacific/Noumea',
        'Papeete': 'Pacific/Tahiti',
        'Apia': 'Pacific/Apia',
        'Nuku\'alofa': 'Pacific/Tongatapu',
        'Port Vila': 'Pacific/Efate',
        'Honiara': 'Pacific/Guadalcanal',
        'Majuro': 'Pacific/Majuro',
        'Tarawa': 'Pacific/Tarawa',
        'Funafuti': 'Pacific/Funafuti',
        'Nuku\'alofa': 'Pacific/Tongatapu',
        
        # Caribbean
        'Havana': 'America/Havana',
        'Kingston': 'America/Jamaica',
        'Santo Domingo': 'America/Santo_Domingo',
        'Port-au-Prince': 'America/Port-au-Prince',
        'San Juan': 'America/Puerto_Rico',
        'Bridgetown': 'America/Barbados',
        'Port of Spain': 'America/Port_of_Spain',
        
        # Central America
        'Guatemala City': 'America/Guatemala',
        'Belize City': 'America/Belize',
        'Tegucigalpa': 'America/Tegucigalpa',
        'Managua': 'America/Managua',
        'San José': 'America/Costa_Rica',
        'Panama City': 'America/Panama',
        
        # UTC Reference
        'UTC': 'UTC'
    }

    selected = ['New York', 'London', 'Sydney']

    if request.method == 'POST':
        selected = [
            request.form.get('city1'),
            request.form.get('city2'),
            request.form.get('city3')
        ]

    times = {}
    for city in selected:
        tz = available_cities.get(city, 'UTC')
        tz_time = datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S")
        times[city] = tz_time

    return render_template(
        'world_clock.html',
        times=times,
        cities=available_cities.keys(),
        selected=selected
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)