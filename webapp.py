from flask import Flask, render_template, request, jsonify
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
    # Get all available timezones from pytz
    all_timezones = sorted(pytz.all_timezones)
    
    # Default selected timezones
    selected = ['America/New_York', 'Europe/London', 'Australia/Sydney']

    if request.method == 'POST':
        selected = [
            request.form.get('city1'),
            request.form.get('city2'),
            request.form.get('city3')
        ]

    times = {}
    for timezone in selected:
        if timezone and timezone in all_timezones:
            tz_time = datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d %H:%M:%S")
            times[timezone] = tz_time

    return render_template(
        'world_clock.html',
        times=times,
        cities=all_timezones,
        selected=selected
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)