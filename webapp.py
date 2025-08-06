from flask import Flask, render_template
from datetime import datetime

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)